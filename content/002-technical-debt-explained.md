Title: Technical Debt Explained
Date: 2021-01-04 21:50
Category: Software Development
Slug: technical-debt-explained


## What is technical debt in software development

Technical debt is the cumulative effect of all the tradeoffs made during the development of software that emphasizes short-term gains over long-term maintainability.

We measure technical debt as the cost of additional work required to move from a relatively poorly designed solution to an optimal solution.

## The analogy of financial debt

If technical debt is not repaid, it can accumulate 'interest', making it harder to implement changes.

And unaddressed technical debt increases software entropy. Ward Cunningham summarized it in an elegant manner:

> "Shipping first time code is like going into debt. A little debt speeds development so long as it is paid back promptly with a rewrite... The danger occurs when the debt is not repaid. Every minute spent on not-quite-right code counts as [interest](https://en.wikipedia.org/wiki/Interest) on that debt. Entire engineering organizations can be brought to a stand-still under the debt load of an unconsolidated implementation, [object-oriented](https://en.wikipedia.org/wiki/Object-oriented_programming) or otherwise."
— [Ward Cunningham](https://en.wikipedia.org/wiki/Ward_Cunningham), 1992

## Acceptance of the technical debt

> "Technical debt is bad, but (more often than not) optimal."
[Paul Graham](http://www.paulgraham.com)

Technical debt is not necessarily a bad thing, and sometimes it is required to move projects forward.

Especially for young start-ups,  accruing technical debt makes perfect sense. The rational behind is: pay for today’s progress with tomorrow’s efforts, until it’s clear whether the company will survive in the market. It’s simple economics. Since most startups fail, high chances are the company will simply fail and the debt will never need to be paid.

This is what we would call a deliberate debt in opposition to another form: non-deliberate technical debt. Deliberate debt happens when Technology and Business teams are aligned. The goal of the organization is to:

- Deliver progress faster
- Reach the product-market fit faster

While keepin in mind that the engineering team is accumulating technical debt that must be paid eventually.

## When the technical debt becomes a problem

Once a company has achieved “product-market fit” and is off to the races, it’s no longer a great idea to just stack debt on top of debt.

The real problem with accumulating technical debt is that the business will never want to pay it off. Stakeholders and the rest of the company might have trouble relating to the abstract nature of resolving technical debt. Senior management might hear: “engineering is requesting permission to move at half pace for the next 3 months.” when engineering is talking about technical debt. Paying off the technical debt ends up being a very difficult thing to rally stakeholder support for.

There is usually no trigger to address the technical debt issue: The impact on the velocity is slow and cumulative that we do not experience it suddenly. We learn to live with it.

We tend to accept as a matter of fact the consequences of the technical debt:

- Disalignment between Technology and Business team: There is a feeling of constant misunderstanding between the two teams
- Slow down of progress: It is more and more difficult to build new features and functionalities
- Impact on the performance and stability: Software become a house of cards, the smallest change might have terrible consequences

## The Death by Tech Debt

Death-by-tech-debt is a slow kind of death. Let's explore some consequences of the tech debt to understand better how it can kill a business.

We can distinguish cash costs vs non-cash cost issues.

Some examples of cash cost consequences of technical are:
- Need to recruit more people to maintain the system
- Extra time required to build new features
- Fines due to security breaches (e.g. SLA)
- Lost sales following the system outages (e.g. churn)

The non-cash costs of the tech debt can also be pretty harmful to a business: For instance, the tech debt can make the engineer team incapable to adapt to the changes in the market.

## Signs of Technical Bankruptcy

If you have any of the following signs, it is undoubtly time to take actions:

- The company sidelines engineering’s concerns as a nice-to-have
- The developers complain about the codebase becoming quite literally a “difficult work environment”
- New features start shipping very slowly. Or stop altogether
- Gradual attrition of all engineers who like building things until only “maintenance-style” engineers remain
- Company falls irrecoverably behind the times

Eventually the codebase goes bankrupt. And the only practical choice will be to rebuild the entire thing from the ground up

## Conclusion

Non-tech executives must understand that if the engineers have been release great things for the past year or so, chances are they’re selling a bit of the future to do it. This is normal. But be prepared for the bill to come due.

Incremental payment of technical debt is better, much like slowly paying off a line of credit. It’s something that can be consciously incorporated into engineering operations while also investing in new work.

But engineering teams need buy-in from management to do this well. When your engineering team talks about technical debt, listen. Listen like you would listen to the finance team talking about financial debt.

The future of your business could very well depend on it: The cost of never paying down this technical debt is clear; eventually the cost to deliver functionality will become so high and the speed of it so slow that it is easy for a well-designed competitive software product to overtake the badly-designed software in terms of features.
