# Digital World

This repository will be updated at the end of every week with code for each Problem Set, and comments to explain the code if necessary.

## How to Use
```
git clone https://github.com/causztic/digital-world
git pull
```

## Contributing
Want to help? Fork this repo and submit a pull request!

https://help.github.com/articles/working-with-forks/

https://help.github.com/articles/creating-a-pull-request-from-a-fork/

## Updating the Raspberry Pi
You can set cobra as a host to make your life easier.
```
git remote add cobra cobra@10.21.146.155:/home/cobra/digital-world.git

git push cobra master

ssh cobra@10.21.146.155
cd ~/digital-world
git pull
```
