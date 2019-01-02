# Setup

```
git clone https://github.com/yanyang729/yanyang729.github.io-src.git --recurse-submodules
pipenv shell
pipenv install

pelican-themes --install ./pelican-themes/Flex

# add Markdown content...

# generate html files
make html

# commit changes and push to output repo
git add .
git commit -m 'new'
gcm
git merge [hash]
git push

# commit src changes
git add .
git commit -m 'fix'
git push
```
