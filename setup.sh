#!/bin/bash

# Check if Chocolatey is installed
if ! command -v choco &>/dev/null; then
  echo "Chocolatey is not installed. Installing..."
  if [[ "$OS" == "Windows_NT" ]]; then
    iwr https://chocolatey.org/install.ps1 -useb | iex
    choco feature enable -n allowGlobalConfirmation
  fi
fi

# Check if Python is installed
if ! command -v python &>/dev/null; then
  echo "Python is not installed. Installing..."
  if [[ "$OS" == "Windows_NT" ]]; then
    choco install python
  else
    sudo apt-get install python
  fi
fi

# Check if pip is installed
if ! command -v pip &>/dev/null; then
  echo "pip is not installed. Installing..."
  if [[ "$OS" == "Windows_NT" ]]; then
    choco install pip
  else
    python -m ensurepip
  fi
fi

# Install the python_mlb_statsapi library
echo "Installing python_mlb_statsapi..."
pip install python_mlb_statsapi

# Check if the library was installed successfully
if ! pip show python_mlb_statsapi &>/dev/null; then
  echo "Failed to install python_mlb_statsapi."
  exit 1
fi

echo "Successfully installed python_mlb_statsapi."
exit 0
