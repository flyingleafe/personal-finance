{
  description = "Monorepo for personal finance tools in Python";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        pythonEnv = pkgs.python311.withPackages (ps: with ps; [
          virtualenv
        ]);
      in
      {
        devShell = pkgs.mkShell {
          buildInputs = [ pythonEnv pkgs.pdm ];

          shellHook = ''
            export PDM_IGNORE_SAVED_PYTHON=1
            eval "$(${pkgs.pdm}/bin/pdm venv activate)"
          '';
        };
      });
}