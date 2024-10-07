# RSA Factoring Challenge

## Introduction
This project focuses on factorizing large numbers, a core challenge in RSA encryption. The goal is to factorize numbers that were used to encrypt important documents over an unsecured network. Some of these numbers may not have been generated using sufficiently large prime numbers, providing an opportunity to factor them and decrypt the documents.

## Objectives
Your mission is to:
- Factorize numbers as quickly as possible before the server fixes the vulnerability.
- Decrypt encrypted documents using the factorized numbers.

## General Information
- **Project Start Date**: Sep 23, 2024, 6:00 PM
- **Project End Date**: Oct 6, 2024, 6:00 PM
- **Checker Release Date**: Sep 27, 2024, 12:00 AM
- **Auto Review**: An auto review will be launched at the deadline.

## Requirements
- You can choose any programming language of your choice to complete the tasks.
- The operating system used must be **Ubuntu 20.04 LTS**.

## Task Overview

### 0. Factorize All the Things!
**Goal**: Factorize as many numbers as possible into the product of two smaller numbers.

- **Usage**: `factors <file>`
  - `<file>` contains natural numbers, one per line.
  - All lines will contain valid natural numbers greater than 1.
  - The file will end with a new line.

- **Output Format**: `n=p*q` (One factorization per line)
  - `p` and `q` don’t need to be prime numbers.

- **Conditions**:
  - You can process the numbers in any order.
  - The program must run without dependencies; nothing can be installed on the machine.
  - Execution time limit: 5 seconds.

### 1. RSA Factoring Challenge
**Goal**: Factorize RSA numbers into their prime components.

- RSA numbers are products of two prime numbers: `n = p * q`.
- Your goal is to find the prime numbers `p` and `q`, given only `n`.

**Key Constraints**:
- Only one number is present in the file.
- Factorize the number as fast as possible, within 5 seconds.

## Example of Factorization
For instance, factorizing the number 6 would result in `6=3*2`.

## Repository
All tasks and scripts related to the RSA Factoring Challenge should be pushed to the following GitHub repository:

- **GitHub Repository**: `RSA-Factoring-Challenge`

