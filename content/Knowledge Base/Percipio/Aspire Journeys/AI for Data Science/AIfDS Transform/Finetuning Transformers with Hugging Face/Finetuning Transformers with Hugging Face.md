# Finetuning Transformers with Hugging Face

## Overview

You’ve been asked by a Frankenstein superfan to finetune a custom model that can write original Frankenstein fanfiction ahead of this year’s Halloween.

You have two options in accomplishing this task. You can either perform QLoRA on the Mistral 7B language model, or perform a full finetune on Distil GPT-2.

You will perform these tasks in finetuning the model:

Import and perform EDA on a dataset made of snippets from Frankenstein
Convert data from Pandas into Hugging Face Datasets and tokenize the data
If you’re doing QLoRA:
Shrink a generative language model with 4bit quantization
Configure LoRA to train a small subset of the quantized model’s parameters
Configure and train the finetuned model
Evaluate and compare the base model and the finetuned model using both perplexity and more informal methods

## Setup

Each step on the kanban board to the right will be flagged with a comment in the project notebook (i.e., Step 1 will be marked with # Step 1 so you can find it.)

You have some choice in this project as to how you’ll perform this finetuning. The choice you make will depend on whether or not you have access to a Graphics Processing Unit (GPU), whether on your local device or via a cloud provider.

If all options are available to you, we recommend doing this project on Google Colab.

Option 1: QLoRA with Mistral7B
Download Mistral 7B GPU notebook using the following link: https://static-assets.codecademy.com/Courses/finetuning-transformer-models/FrankensteinGPUStarter.zip

When you should choose option 1
You can choose Mistral 7B, a cutting-edge 7 billion parameter language model, if you meet one of the following conditions:

You’re allowed to use Google Colab (https://colab.research.google.com) where you are
You need to be logged into Google to use Colab, so make sure that’s OK too
You are comfortable using Paperspace Gradient (https://paperspace.com/notebooks), Kaggle (https://kaggle.com), or similar cloud notebook providers
You have a personal computer with an NVIDIA GPU
Setup Guide
Let’s assume you’re using Colab.

First, head to https://colab.research.google.com and select the “Upload” option on the sidebar of the “Open notebook” screen. Then navigate to wherever you downloaded and unzipped the project folder and select the notebook.

Now make sure you’re using the GPU by navigating to “Runtime > Change runtime type” and selecting the T4 GPU.

Next, click on the folder icon on the left-hand side of Colab. Ensure you’re connected to the runtime and select the upload file icon (furthest left). Track down frankenstein_chunks.csv and select it. Now you’re ready to follow along with the project.

If you’re using Paperspace or another cloud notebook provider, the process is mostly the same, though you’ll have to find all the relevant options in the UI yourself. And if you’ve got a big enough GPU to perform this project locally, we’ll assume you know how to get yourself started.

Option 2: DistilGPT-2 on the CPU
Download DistilGPT2 CPU notebook with the following link: https://static-assets.codecademy.com/Courses/finetuning-transformer-models/FrankensteinCPUStarter.zip

When you should choose option 2
If none of those options are available to you, no problem. You can still use DistilGPT-2 with this lesson and you’ll perform a full finetune. This is a good option if you both:

Are at work and aren’t allowed to log into Google for security reasons
Don’t have a powerful enough graphics card to finetune Mistral7B
Setup Guide
Open the unzipped project folder in your IDE of choice and get started!

## Resources

This project will only challenge you on concepts and syntax we’ve already covered in this course. You may want to open the exercises from the previous lesson in another tab to easily look up the relevant notebooks.

If you get stuck, consult the following solutions notebooks:

GPU Solution Notebook: https://static-assets.codecademy.com/Courses/finetuning-transformer-models/FrankensteinGPU.ipynb
Reminder: This notebook will only work if you have access to a GPU, either locally or via a cloud notebook provider like Colab.

CPU Solution Notebook https://static-assets.codecademy.com/Courses/finetuning-transformer-models/FrankensteinMPSCPU.ipynb
If you’d like to learn more about the models we’re using, you can find them by their Hugging Face model cards, for starters:

https://huggingface.co/mistralai/Mistral-7B-v0.1

https://huggingface.co/distilbert/distilgpt2

The original text of Shelley’s Frankenstein was obtained via Project Gutenberg: https://www.gutenberg.org/ebooks/84

