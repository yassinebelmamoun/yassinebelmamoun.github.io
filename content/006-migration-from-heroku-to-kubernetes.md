Title: From PaaS to K8s: Lessons Learned on Our Startup's Infrastructure Journey
Date: 2024-05-17 12:00
Category: Software Engineering
Slug: migration-from-paas-to-kubernetes
status: draft

You've probably heard the advice a million times: when you're starting a new software project or company, just focus on building your product and creating value for customers. Don't get bogged down in infrastructure and DevOps. Use a Platform-as-a-Service (PaaS) like Heroku and iterate quickly.

This is 100% the right call in the beginning. When we founded Manatal, we hosted everything on Heroku initially. It allowed us to rapidly develop our software without worrying about servers, deployments, scaling, etc. We could push new code and features fast.

But there comes a point, as your startup grows, where you start pushing the limits of a PaaS. You need more granular control, better visibility into your systems, and the ability to optimize performance. About 2 years ago, we reached that inflection point at Manatal. So we decided to take the plunge and migrate our entire infrastructure from Heroku to Kubernetes on AWS.

Was it challenging? Absolutely. Running your own Kubernetes clusters is no joke, especially compared to the simplicity of a PaaS. Suddenly you're on the hook for cluster management, the full CI/CD pipeline, monitoring, security, and a whole lot more. A lot more power but a lot more responsibility too.

We had to level up our skills across the board - from containerizing microservices to deploying infrastructure-as-code. We evaluated different approaches and made opinionated choices. Kustomize instead of Helm. ArgoCD for continuous deployment. Datadog for observability. GitHub Actions for CI. KEDA and cluster-autoscaler for intelligent scaling. The list goes on.

But now, I can confidently say it was worth it. We have so much more control and visibility now. When issues emerge, we can dive deep. We can tweak and optimize every layer.

We also realized huge performance gains and cost savings compared to Heroku's more constrained (and expensive) resources. With the ability to use custom machine types and dynamic scaling based on load, our utilization is way up and our hosting bill is way down. But those savings don't just pad our bottom line. They go directly into making our product better, faster, and more feature-rich for our customers. Every dollar saved is a dollar invested in delivering more value to them.

Migration to Kubernetes also forced us to modernize our architecture and development processes in a good way. Decomposing monoliths into microservices. Defining resources declaratively. Automating everything. Committing to gitops and immutable deployments. It can be a painful upgrade but you come out the other side as a more mature engineering organization.

Now, I won't sugarcoat it. Kubernetes is complex and it's not the right choice for every company. You need to assess your team's capabilities and your scale needs realistically. Start with a PaaS. Squeeze everything you can out of that model. But when you're ready to unlock the next level of performance and control, Kubernetes will be waiting for you. The lessons you learn along the way will make you a better technologist.

If you're considering making the jump from Heroku to Kubernetes on AWS like we did, here's a detailed rundown of what you'll need to learn and the tools we recommend:

1. **Containerization:** Get comfortable with Docker and learn how to package your application into containers. This involves writing Dockerfiles, optimizing image sizes, and pushing images to a container registry. We use Amazon Elastic Container Registry (ECR) for storing and managing our Docker images securely.
2. **Kubernetes Concepts:** Master the fundamentals of Kubernetes architecture, including Pods, Services, Deployments, StatefulSets, and more. Learn how to define and manage application configurations using Kubernetes manifests. We use Kustomize for templating and managing Kubernetes manifests in a more modular and maintainable way.
3. **EKS Cluster Management:** Learn how to create, configure, and operate Kubernetes clusters on AWS using EKS. This involves defining worker node groups, configuring the Kubernetes API server, setting up IAM roles, and integrating with other AWS services. We use eksctl, a powerful CLI tool, to simplify EKS cluster creation and management.
4. **Observability Stack:** Build a robust monitoring and logging solution for your Kubernetes clusters and applications. We use Datadog for log management and application performance monitoring (APM). It provides deep visibility into cluster health, resource utilization, and application metrics.
5. **Gitops Workflow:** Embrace gitops principles and define all your infrastructure and application configurations as code in Git repositories. We use ArgoCD for continuous deployment and synchronization of our Kubernetes manifests. It ensures that our deployed applications always match our desired state defined in Git.
6. **AWS Ecosystem Integration:** Familiarize yourself with the broader AWS ecosystem and learn how to integrate Kubernetes with other AWS services. For example, we use AWS Secrets Manager for securely storing and managing secrets, and Kubernetes external-secrets to sync those secrets into our clusters.
7. **Scaling and Optimization:** Learn how to scale your Kubernetes applications efficiently. We use Kubernetes Horizontal Pod Autoscaler (HPA) and Cluster Autoscaler to automatically adjust the number of pods and nodes based on resource utilization. For more advanced scaling scenarios, we leverage Kubernetes Event-Driven Autoscaling (KEDA).
8. **Development Workflow:** Adopt a smooth development workflow for building, testing, and deploying your applications. We use GitHub Actions for continuous integration (CI) pipelines to build and test our code changes automatically. For local Kubernetes development and troubleshooting, we rely on tools like kubectl and K9s, a terminal-based UI for interacting with Kubernetes clusters.

Remember, the journey to Kubernetes proficiency is gradual. Start with the basics, experiment with different tools, and learn from the vibrant Kubernetes community. As you gain experience, you'll be able to optimize your infrastructure further and tackle more advanced scenarios.
Embracing Kubernetes on AWS has been a game-changer for our startup, enabling us to scale seamlessly, improve efficiency, and unlock new possibilities. If you're ready to embark on this transformative journey, dive in with curiosity and determination. The effort you put in will pay off greatly in the long run.