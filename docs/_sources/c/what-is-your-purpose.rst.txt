What is your purpose?
=====================

.. note::  This content is still work in progress. If you have ideas that you would want to contribute to - please `raise a PR <https://github.com/rajatpandit/platform-engineering-success/pulls>`_

My experience regarding platform engineering goes back to running a team that initially was seeded with the idea of managing the centrally run developer tools. We also had a number of build engineers who were graduating into the devops skills. This team was primarily deployed in various product engineering teams as the resident 'devops engineers'. However in the regular reviews with these two teams it was the evident that there was a vicious cycle of redundant and duplicate work. The resident devops engineering would essentially spend their time in the in the following order
* Setting up base infrastructure - various environments etc. - usually in cloud
* Setup a CI/CD framework - usually jenkins capable of deployment to these environments
* Integrate environments with the enteprise standard solutions like centralised logging, monitoring and observability systems
* Worse off - at the behest of the engineering teams at times create local instances of the enterprise standard solutions
* Since this was mandatory for any go-live the environment would go through the pentetration testing

Ones this was setup. The devops engineer would either get reduced to the reduced to the ops guy managing production issues or start to hand over to the engineers who were already over loaded with items in the backlog that had to be shipped yesterday. 

The central team also had its interesting share of challenges. The teams that managed would adhoc requests from these initial engineering teams regarding integration. Often their non functional requirements wouldn't be thought through or wasn't centrally managed. This meant the sizing of the central environment would always run in the risk of either being over provisioned - costing more or under provisioned running the risk of reduced availability. The central team also had to scale to support the various point to point integrations with the various business units - which meant the rate at which the central teams could do their upgrades had to be managed carefully to reduce the risk of downtimes. This overall reduced the pace of innovation that the central tools team could provide. 




You are a technology leader and you are trying to give examples of why companies should invest in building a platform engineering team. Here are some possible reasons:

create and maintain a common set of tools, frameworks, and standards that enable faster and more reliable delivery of software products and services across the organization.
foster a culture of collaboration, innovation, and feedback among developers, testers, operations, and business stakeholders by providing a shared vision and roadmap for the platform.
reduce costs and risks by optimizing the use of cloud resources, ensuring compliance with security and regulatory requirements, and implementing best practices for monitoring, logging, and troubleshooting.
drive business value by enabling new capabilities, features, and integrations that enhance the user experience and satisfaction of the customers and partners.


Some possible benefits of having a platform engineering team in an organisation are:

accelerate the delivery of applications and the pace at which they produce business value by providing self-service capabilities with automated infrastructure operations.
Improve developer experience and productivity by offering common, reusable tools and capabilities, and interfacing to complex infrastructure.
Optimize the developer experience and reduce friction for the valuable work they do by building operating platforms that sit between the end user and the backing services on which they rely.
Solve the central problem of cooperation between software developers and operators by creating and maintaining the software infrastructure used by other engineering and IT teams .
Build development tools that multiple product engineering teams can use, and maintain them until they are decommissioned.


Help product teams navigate the increasing complexity of modern software architectures and cloud services by providing curated and integrated solutions .



Some possible risks of having a platform engineering team in an organisation are:

- The platform team may become a bottleneck for the product teams if they cannot deliver the required tools and capabilities in a timely manner.
- The platform team may lose alignment with the product teams if they do not communicate effectively and understand their needs and priorities.
- The platform team may create unnecessary complexity or duplication if they do not coordinate with other platform teams or leverage existing solutions.
- The platform team may face challenges in measuring their impact and value if they do not define clear metrics and feedback mechanisms.
- The platform team may struggle to attract and retain talent if they do not offer a compelling vision and career path for platform engineers.


Some possible cost implications of having a platform engineering team in an organisation are:

- The platform engineering team requires skilled and experienced engineers who can design, build and maintain the platform infrastructure and services. This means that the organisation needs to invest in hiring, training and retaining such talent, which can be costly and competitive in the market.
- The platform engineering team needs to have access to adequate resources and tools to support the platform development and operations. This includes hardware, software, cloud services, security systems, monitoring tools, etc. The organisation needs to allocate sufficient budget and time for procuring, deploying and updating these resources and tools, which can also incur significant costs.
- The platform engineering team needs to collaborate and communicate effectively with other teams in the organisation, such as product teams, business teams, security teams, etc. This means that the organisation needs to establish clear roles and responsibilities, governance models, service level agreements, feedback mechanisms, etc. The organisation needs to invest in creating and maintaining a culture of trust, transparency and alignment among the teams, which can require time and effort.


As a technology leader, you have a responsibility to ensure that your organization is delivering high-quality software products and services that meet the needs and expectations of your customers and stakeholders. One of the ways to achieve this is by setting up a platform engineering team that can provide a common set of tools, processes, and standards for your software development teams. In this document, I will make a strong technical and business case for establishing a platform engineering team and address the potential risks associated with it.

- A platform engineering team can help you improve the efficiency and effectiveness of your software development teams by:
  - Providing a consistent and reliable environment for developing, testing, deploying, and monitoring software applications across different platforms and technologies.
  - Reducing the duplication of effort and resources by creating reusable components, libraries, frameworks, and services that can be shared and integrated by multiple teams.
  - Enabling faster delivery and feedback cycles by automating and streamlining the software development lifecycle (SDLC) processes such as code review, testing, integration, deployment, and release management.
  - Enhancing the quality and security of your software products and services by enforcing best practices, standards, and policies for code quality, performance, scalability, reliability, availability, and compliance.
  - Supporting innovation and experimentation by providing a sandbox environment where teams can prototype, test, and validate new ideas and technologies without affecting the production systems.

- A platform engineering team can help you increase the value proposition and reduce the opportunity cost of your software products and services by:
  - Improving the customer satisfaction and retention by delivering software products and services that are faster, more reliable, more secure, more user-friendly, and more aligned with their needs and expectations.
  - Increasing the market share and revenue by enabling faster time-to-market, shorter feedback loops, more frequent updates, and more competitive differentiation of your software products and services.
  - Reducing the operational cost and risk by minimizing the downtime, errors, defects, incidents, vulnerabilities, and technical debt of your software products and services.
  - Leveraging the economies of scale and scope by optimizing the utilization of your infrastructure, resources, and capabilities across different software products and services.

- A platform engineering team can help you mitigate the technical and business risks associated with setting up a platform engineering team by:
  - Conducting a thorough assessment of your current state of software development practices, processes, tools, technologies, challenges, gaps, and opportunities.
  - Developing a clear vision, strategy, roadmap, architecture, design, governance model, success metrics, and communication plan for your platform engineering initiative.
  - Engaging with your stakeholders from different business units, functions, domains, teams, roles, levels to understand their needs, expectations, concerns, feedbacks regarding your platform engineering initiative.
  - Building a cross-functional platform engineering team with the right mix of skills, expertise,
experience,
and culture fit for your organization.
  - Implementing an agile and iterative approach for delivering incremental value to your stakeholders while ensuring continuous improvement and learning from your platform engineering initiative.