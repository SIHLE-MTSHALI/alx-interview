# 0x06. Star Wars API

This project interacts with the Star Wars API to fetch and display characters from a specific movie.

## Files

- `0-starwars_characters.js`: Main script to fetch and display Star Wars characters.

## Setup

1. Install Node.js 10.x:

curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs

2. Install the `request` module:

sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules

## Usage

Run the script with a movie ID as an argument:

./0-starwars_characters.js 3


This will display the characters from the movie with ID 3 (Return of the Jedi).
