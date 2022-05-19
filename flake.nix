{
  description = "Feature Engineering Examples";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-21.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }: let

    # each system
    eachSystem = system: let
      config = { allowUnfree = true;};
      pkgs = import nixpkgs {
        inherit system;
        inherit config;
        overlays = [ self.overlay ];
      };
      pyenv = pkgs.python3.withPackages (p: [ p.numpy p.pytest ]);

    in rec {
      devShell = pkgs.mkShell {
        buildInputs = with pkgs; [ pyenv nodejs ];
      };
    }; # eachSystem

    overlay = final: prev: {
    };

  in
    flake-utils.lib.eachDefaultSystem eachSystem // { inherit overlay; };
}
