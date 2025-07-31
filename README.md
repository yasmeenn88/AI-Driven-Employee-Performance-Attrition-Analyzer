#  HR Attrition Prediction

##  Dataset Overview

**Source:** [Kaggle - HR Attrition Dataset](https://www.kaggle.com/datasets/ankitrajmishra/hr-attrition-dataset)

Employee attrition is a critical issue faced by organizations, especially in competitive industries like IT and services. Losing employees not only affects productivity but also increases costs related to hiring, training, and onboarding.

---

## 🧾 Column Descriptions

| Column Name                             | Description                                                                 |
|-----------------------------------------|-----------------------------------------------------------------------------|
| `Employee_ID`                           | Unique identifier assigned to each employee.                                |
| `Age`                                   | Employee's age.                                                             |
| `Attrition`                             | Whether the employee has left the company (`Yes`/`No`).                     |
| `Business_Travel`                       | Frequency or type of business travel.                                       |
| `Department`                            | Department where the employee works.                                        |
| `Distance_From_Home`                    | Distance between the employee's home and workplace.                         |
| `Education`                             | Employee's education level.                                                 |
| `Environment_Satisfaction`              | Rating of work environment satisfaction (1 = Low, 5 = High).                |
| `Gender`                                | Gender of the employee.                                                     |
| `Salary`                                | Employee’s salary.                                                          |
| `Job_Involvement`                       | Manager’s rating of job involvement (1 to 5).                               |
| `Job_Level`                             | Job level within the company (1 = Lowest, 8 = Highest).                     |
| `Job_Role`                              | Specific role (e.g., HR, Developer, Manager, Technician, etc.).             |
| `Job_Satisfaction`                      | Employee’s job satisfaction rating (1 to 5).                                |
| `Marital_Status`                        | Employee's marital status.                                                  |
| `Number_of_Companies_Worked_Previously` | Total number of companies previously worked for.                            |
| `Overtime`                              | Indicates if the employee works overtime (`Yes`/`No`).                      |
| `Salary_Hike_in_Percent`                | Percentage increase in salary.                                              |
| `Total_Working_Years_Experience`        | Total working experience across all jobs.                                   |
| `Work_Life_Balance`                     | Self-rating of work-life balance (1 to 5).                                  |
| `No_of_Years_Worked_at_Current_Company` | Total years at the current company.                                         |
| `No_of_Years_in_Current_Role`           | Total years in the current role.                                            |
| `Years_Since_Last_Promotion`            | Number of years since the last promotion.                                   |

-----
##  Goal: Predicting Employee Attrition

The objective of this project is to build a machine learning model that can accurately **predict whether an employee is likely to leave the company** (Attrition = `Yes`) or stay (Attrition = `No`).

Understanding employee attrition allows HR teams to proactively address workplace issues, improve employee satisfaction, and reduce turnover costs.

Below is the class distribution of the target variable `Attrition`:

![Class Distribution](images/classes.png)

