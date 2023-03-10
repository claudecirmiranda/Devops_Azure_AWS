# Solução de DevOps MultCloud

![Devops MultCloud](https://raw.githubusercontent.com/claudecirmiranda/Devops_Azure_AWS/main/aws_and_azure_devops_solution.png)

Este repositório descreve a arquitetura de uma solução de DevOps MultCloud que utiliza serviços tanto da **AWS** quanto da **Azure**. A solução visa proporcionar flexibilidade e escalabilidade na gestão de aplicações em ambientes de nuvem.

## AWS DevOps

A solução de DevOps na AWS consiste nos seguintes componentes:

* Gerenciamento de Código-Fonte: CodeCommit
* Build e Teste: CodeBuild
* Implantação: CodeDeploy, Grupo de Escalonamento Automático e ELB
* Infraestrutura: Instâncias EC2, Banco de Dados RDS e Bucket S3
* CodePipeline conecta todos os componentes em um pipeline de integração e implantação contínua.

## Azure DevOps

A solução de DevOps na Azure consiste nos seguintes componentes:

* Gerenciamento de Código-Fonte: Azure Repos
* Build e Teste: Azure Pipelines
* Implantação: Slots de Implantação do Azure, AKS e Load Balancer
* Infraestrutura: Serviços de Aplicação, Banco de Dados SQL e Conta de Armazenamento
* Azure DevOps conecta todos os componentes em um pipeline de integração e implantação contínua.

## Escolhas de Solução

A solução de DevOps MultCloud escolhida visa aproveitar as vantagens de cada provedor de nuvem e proporcionar uma integração suave entre os componentes de DevOps. Além disso, a solução permite que as equipes de desenvolvimento possam trabalhar com a nuvem de sua preferência, sem limitações na gestão de aplicações.

Com esta solução, é possível garantir uma gestão eficiente de aplicações em ambientes de nuvem, oferecendo escalabilidade e flexibilidade para atender às demandas do negócio.

## Tabela de requisitos não funcionais

| Requisitos não funcionais | AWS | Azure | Solução |
| --- | --- | --- | --- |
| Escalabilidade | EC2 com Auto Scaling Group | AKS | Auto Scaling |
| Disponibilidade | ELB | Load Balancer | Load Balancing |
| Desempenho | EC2 instances | App Services | Compute |
| Segurança | Codecommit, Codebuild, Codedeploy, Codepipeline | Azure Repos, Azure Pipelines, Azure Deployment Slots, Azure DevOps | Source Code Management and Continuous Integration/Delivery |
| Armazenamento | S3 Bucket | Storage Account | Storage |
| Banco de Dados | RDS Database | SQL Database | Database |
