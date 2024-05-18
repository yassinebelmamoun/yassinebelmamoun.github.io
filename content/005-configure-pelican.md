Title: Pelican Tutorial
Date: 2023-10-22
Category: Content Creation
Slug: pelican-tutorial
status: draft

This article is in draft mode.

# Objectives
- Install Pelican & create your blog locally
- Create your first article
- Customise your theme
- Publish to GitHub Pages
- Automate with Github Actions

# Step 1: Install Pelican

I use `pipenv` to manage all my python project.

```sh
mkdir -p ~/repos/my-blog
pipenv install pelican markdown
pipenv shell
```

# Step 2: Quick-start your Pelican project

Pelican offers a command to quickly build your project from scratch

```sh
pelican-quickstart
```

# Step 3: Create your first article and run your devserver



# Reference

- [Pelican Documentation](https://docs.getpelican.com/en/latest/)