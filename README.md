# ParaBank Project Testing automation with python BDD selenium framework

This testing document is intended for the development team, testing team, and other stakeholders involved in the ParaBank Banking project. Additionally, it aims to provide a clear understanding of the testing process for all those interested in the quality and performance of the application.

## Revision History:

| Date       | Description                   | Author            | Comments          |
| ---------- | ----------------------------- | ------------------ | ------------------ |
| 26.02.2024 | Test Plan for version 1.0     | Pricopie Adrian   | Draft test plan    |
| 1.03.2024 | v1.1                          | Robert Furtuna    | Added more details for Test Process |

## Table of Content:
1. [Introduction](#introduction)
   - [Project Objective](#project-objective)
   - [Functionalities in Scope](#functionalities-in-scope)
   - [Functionalities and Tests Out of Scope](#functionalities-and-tests-out-of-scope)
2. [Test Process](#test-process)
   - [Test Planning](#test-planning)
     - [Roles and Responsibilities](#roles-and-responsibilities)
     - [Entry Criteria](#entry-criteria)
     - [Exit Criteria](#exit-criteria)
     - [Risks](#risks)
   - [Test Analysis](#test-analysis)
   - [Test Design](#test-design)
   - [Test Implementation](#test-implementation)
   - [Test Execution](#test-execution)
   - [Test Closure](#test-closure)
   - [Test Monitoring and Control](#test-monitoring-and-control)
3. [Test Deliverables](#test-deliverables)
   - [Test Conditions](#test-conditions)
   - [Test Cases](#test-cases)
   - [Daily Test Summary Reports](#daily-test-summary-reports)
   - [Traceability Matrix](#traceability-matrix)
   - [Test Case Results](#test-case-results)
   - [Bugs Report](#bugs-report)
   - [Test Completion Report](#test-completion-report)
   - [Schedule](#schedule)

## Introduction:
- ParaBank is a demo site used for demonstration of Parasoft software solutions.
All materials herein are used solely for simulating a realistic online banking website.

### 1.1 Project Objective

- We need to raise the trust in the quality of the project as high as possible before releasing it to customers.
- Application under test: [ParaBank](https://parabank.parasoft.com/parabank/index.htm).

### 1.2 Functionalities in Scope
- testing will primarily concentrate on the Chrome browser. 
- To ensure the quality and functionality of the ParaBank platform, the following functionalities will be included in functional testing and graphical user interface (GUI) testing: Forgot password, login, customercare, register.
- To ensure that new customers can successfully register and access the ParaBank services.
- To ensure that a customer can successfully log in and access the ParaBank services.
- To ensure that if a customer forgot their password, they can recover using the "Forgot Password" functionality.
- To ensure effective customer care functionality is in place, providing support and assistance to users as they interact with ParaBank services.

### 1.3 Functionalities and Tests Out of Scope

- Non-functional testing like stress, performance is beyond the scope of this project.
- No QA support for mobile applications developed. Only web applications will be tested.

# 2. Test Process:

## 2.1 Test Planning

### Roles and Responsibilities:

| Tester                    | Responsibilities                    |
|---------------------------|-------------------------------------|
| Anetta Bako(junior-mid)  | - Customercare testing             |
|                           | - Forgot password testing         |
| Pricopie Adrian(junior)   | - Login  testing                  |
| Robert Furtuna(senior)  | - Register testing  |

### Entry Criteria:

- Roles needed for the project are allocated.
- Functional specifications are defined.
  
