Title: Pelican Tutorial
Date: 2024-05-18
Category: Content Creation
Slug: pelican-tutorial

In my [previous article]({filename}/004-start-your-blog.md), I shared my journey of realizing the importance of creating content and finding the right balance between consuming and producing. This led me to search for the perfect blogging solution that met my specific requirements, and I ultimately chose Pelican, a static site generator built with Python. If you want to learn more about my decision-making process, check out [my article]({filename}/004-start-your-blog.md) on why I chose Pelican for my blog.

Now, let's dive into the process of setting up Pelican locally and deploying your blog to GitHub Pages using Github Actions. By following this tutorial, you'll have a fully customizable, self-hosted blog that's free to maintain.

## Installing Pelican Locally

To get started, install Pelican on your computer by running the following command in your terminal:
```
pip install pelican markdown
```
Next, create a directory for your blog and navigate into it:
```
mkdir my-blog
cd my-blog
```
Then, generate the scaffolding for your blog using Pelican's ﻿quickstart command:
```
pelican-quickstart
```
Answer the prompts, and you'll have the basic structure ready to go.


## Writing and Previewing Blog Posts

To add new posts, create Markdown files in the `content` directory. 
For example, create a file named `my-first-post.md`, open it in your favorite text editor, and add metadata like title, date, category, and tags at the top:
```md
Title: My First Blog Post
Date: 2023-05-18
Category: Blogging
Tags: pelican, python, github

Hello World! Your content starts here.
```

Below the metadata, write your post using Markdown syntax. Pelican's support for Markdown ensures that your content will be reader-friendly and visually appealing.

To preview your blog locally, generate the HTML files and start a local server:
```
pelican content
pelican --listen
```

Open your browser and navigate to `http://localhost:8000` to see your blog in action. Experiment with different themes and settings in `pelicanconf.py` to customize your blog's appearance.

## Configuring GitHub Pages

First, create a new repository on GitHub named `username.github.io`. Then, initialize a new git repository in your blog directory and add the GitHub repository as a remote:
```
git init
git remote add origin https://github.com/username/username.github.io.git
```

Before automating the deployment process with GitHub Actions, you need to configure GitHub Pages for your repository. Follow these steps:

1. Go to the repository's settings by clicking on the "Settings" tab.
2. Scroll down to the "GitHub Pages" section.
3. Under "Source," select the `gh-pages` branch to use for GitHub Pages.
4. Click "Save" to apply the changes.

GitHub Pages will now serve the content from the `gh-pages` branch at `https://yourusername.github.io`.

If you want to use a custom domain for your blog, you can set it up in the "GitHub Pages" section as well. In my case, I use `yassinebelmamoun.com` as my custom domain. To do this:

1. In the "GitHub Pages" section, under "Custom domain," enter your custom domain (e.g., `yassinebelmamoun.com`).
2. Click "Save" to apply the changes.
3. Create a file named `CNAME` in the root of your blog's source branch (e.g., `main` or `master`) and add your custom domain to it (e.g., `yassinebelmamoun.com`).
4. Configure your domain's DNS settings to point to GitHub Pages. You'll need to add a CNAME record or an A record pointing to the GitHub Pages IP addresses. Refer to the GitHub Pages documentation for detailed instructions on configuring your domain.

Once you've completed these steps, your blog will be accessible at your custom domain (e.g., `https://yassinebelmamoun.com`).

## Automating Deployment with GitHub Actions

To automate the deployment of your Pelican blog to GitHub Pages, we'll use GitHub Actions. This way, whenever you push new content or make changes to your blog, GitHub Actions will automatically rebuild and deploy your site.

To do this, create a new file named `.github/workflows/publish-to-ghp.yml` in your repository with the following content:

```yaml
name: Publish to GitHub Pages
on:
  push:
    branches:
      - main
env:
  SITEURL: https://www.yassinebelmamoun.com
jobs:
  deploy:
    runs-on: ubuntu-22.04
    permissions:
      contents: write
    concurrency:
      group: ${{ github.workflow }}-${{ github.ref }}
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.11'
      - name: Upgrade pip
        run: |
          # install pip=>20.1 to use "pip cache dir"
          python3 -m pip install --upgrade pip
      - name: Get pip cache dir
        id: pip-cache
        run: echo "dir=$(pip cache dir)" >> $GITHUB_OUTPUT
      - name: Cache dependencies
        uses: actions/cache@v3
        with:
          path: ${{ steps.pip-cache.outputs.dir }}
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-
      - name: Install dependencies
        run: python3 -m pip install -r ./requirements.txt
      - name: Build site
        run: pelican content -o output -s pelicanconf.py
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v4
        if: github.ref == 'refs/heads/main'
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./output
```


This workflow file instructs GitHub Actions to set up a Python environment, install your requirements, build your Pelican site, and deploy the generated output folder to a branch called `gh-pages` using the `peaceiris/actions-gh-pages` action.

A few important remarks:

- For GitHub Actions beginners: The `GITHUB_TOKEN` is automatically created by GitHub Actions to authenticate your workflow, not a personal access token. It's a special installation access token used to authenticate on behalf of the GitHub App. You can start deploying immediately without any configuration, as the token is available in the GitHub context even if not explicitly passed.
- Make sure that you have `requirements.txt` in your root folder.
- Make sure that you github branch is `main` (instead of `master`)
- Make sure to replace https://yassinebelmamoun.github.io with your Github repository
- Make sure to configure your domain name in your `publishconf.py`


Commit your changes and push to the `main` branch of your GitHub repository:
```
git add .
git commit -m "Set up Pelican blog with GitHub Actions"
git push -u origin main
```

GitHub Actions will automatically trigger the workflow, build your Pelican site, and deploy it to GitHub Pages. After a few minutes, visit your website to see your live blog!

## Embrace the Power of Pelican and GitHub Actions

With Pelican and GitHub Actions working together, you have a powerful and efficient setup for your blog. You can focus on creating amazing content while the automation takes care of the rest.

Thank you for reading this tutorial on setting up Pelican and deploying your blog to GitHub Pages. I hope you found it helpful and informative.