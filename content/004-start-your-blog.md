Title: Blogging made simple
Date: 2023-10-22
Category: Tutorial
Slug: start-your-blog-101


Every week, I invest a substantial amount of time reading, exploring podcasts and watching videos, all in the pursuit of knowledge. However, I've uncovered a missing piece in this quest: passive consumption of information isn't enough, there is immense value in creating content, exposing it to a wide audience to assist others and learn back from them.

That's when I realized that I need to adjust the balance between the amount of content I passively consume and the amount of content that I actively produce. To get things rolling, I wanted to make things super easy for myself to publish articles on this blog. This post is all about sharing my current setup and explaining why and how I set it up this way.

## Choice of a solution

I had the following requirements:

- I needed easy customization for my blog's format and design.
- The content I publish had to be reader-friendly, including support for code syntax highlighting.
- I wanted to steer clear of third-party dependencies like hosted platforms (Medium, Blogger, etc.).
- Writing offline, even on a plane, had to be seamless.
- Budget-wise, I aimed for an economical approach, staying within the range of $20 per year.
- Learning a new technology was a no-go; simplicity was paramount.
- Markdown had to be my go-to format for content creation.
- Lastly, I wanted to avoid the complexities of handling intricate systems, like databases.

I evaluated various solutions, which I categorized as follows:

- Managed Solutions (e.g. Medium, Blogger, Squarespace, etc.)
- Self Hosted Solutions
	- Dynamic Website Generator (e.g. Wordpress)
	- Static Website Generator (e.g. Jekyll, Hugo, Pelican)

Managed solutions were quickly ruled out due to limitations like domain name usage restrictions, cost, and intrusive advertisements, among other issues. My focus shifted to self-hosted alternatives.

I dismissed options like WordPress for being overly complex (e.g. databases), and honed in on lightweight solutions like static website generators—specifically Jekyll, Hugo, and Pelican.

Ultimately, I chose Pelican because it's built with Python, a language I'm comfortable with.

## How it works

Here is a brief of how easy it is to set up:

1. Install the Pelican library locally
2. Run a command to quick start your project
3. (Optional) Configure your project (e.g. themes, etc.)
4. Write articles (and pages) in Markdown
5. Run a command to publish your articles


Producing content is straightforward: all you need is a text editor supporting Markdown. Then, you can track all changes with git history, publish your article with a simple `git push` and host your entire blog on Github Pages.

This setup offers a portable self-hosted blog that's fully customizable. You can write offline, and the best part? It's entirely cost-free (e.g. the only cost would be for acquiring a domain name ~ 10$ per year).

## Tutorial

If you'd like to do the same, the only requirement is a very basic understanding of Python.

I wrote a more detailed tutorial on [how to get started with Pelican]({filename}/005-configure-pelican.md).

