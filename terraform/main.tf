terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  alias  = "us1"
  region = "us-east-1"
}

provider "aws" {
  alias  = "in1"
  region = "ap-south-1"
}

locals {
    env = terraform.workspace
}

module "app_us1" {
  source = "./modules/ec2-instance"
  providers = {
    aws = aws.us1
  }
  name          = "app"
  env           = local.env
  ami           = "ami-12345678"
  instance_type = "t2.micro"
}

resource "null_resource" "setup" {
  provisioner "local-exec" {
    command = "echo Hello from Terraform"
  }
}






