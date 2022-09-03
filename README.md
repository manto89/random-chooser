This is a very basic project aiming at exposing a web page with some random combinations of 3 items from a list of choices

The included docker-compose includes labels used by traefik for deployment
## Installation steps
```
git clone https://github.com/manto89/random-chooser
cd ./random-chooser
docker build --tag random-chooser . 
```
place the choices in input.txt, one per line. The script randomize the choices and picks 3 items, then finally
```
docker-compose up -d
```
