# NDT Requirements list maker
#### Video Demo:  <https://youtu.be/6NrFrcWkIzs>
#### Description:
## Purpose
Nondestructive-Testing(NDT) is a testing and analysis technique used by industry to evaluate the properties of a material, component, structure or system for characteristic differences or welding defects and discontinuities without causing damage to the original part. There are many NDT methods to test the properties of a material,for example, Dye Penetrant Testing(PT), Magnetic-particle testing (MT), Ultrasonic Testing (UT) and Radiographic Testing (RT).

Determining which test to use is according to the standard, which provide established procedures, criteria, and requirements that help ensure consistency, reliability, and comparability of test results.One part of the standard is the NDT requirements list, which provides specific guidelines for testing materials, welding, NDT methods, minimum required efficiency, and final inspection time.

In this project, I have developed a program called "NDT Requirements List Maker" that determines the NTD methods, minimum-required-efficiency and final inspection-time according to the standard. The program can read the NDT list (without NDT methods) located in the folder and write the NDT methods information into it.

## NDT Standard

In differnet industries, there are various standard specifications. In my case, I have established an NDT standard with the following specifications:

### List Format
1. The NDT Requirements List should provide the system name and date as a heading.

2. The NDT Requirements List should include basic information for the NDT Inspector, as follows:
>* Part number
>* Material of Base
>* Material of Parts
>* Structure Category
>* Welding Category
>* Drawing
>* NTD methods (including minimum-required-efficiency and final inspection-time)

### Structure Category
Each inspection object is classified from A to D based structure-category classification used to categorize different types of structures based on their characteristics, complexity, or intended use.The judging criteria are as follows:
|Structure-Category|Description|
| :-------------: |:-------------|
 | A      | Highly complex structures with extremely high requirements, may involve intricate architectural designs, advanced equipment, or critical components.    |
 | B      | Complex structures with high requirements, may include large-scale architectural structures, important equipment, or critical components.     |
 | C      | Structures of moderate complexity with higher requirements, may involve medium-sized architectural structures or critical components.   |
 | D      | Specific structure type with lower complexity and requirements, typically including simple architectural structures or non-critical components.     |

### NDT Methods
The judging criteria for testing methods are as follows:

* Dye Penetrant Testing(PT) and Magnetic-particle testing (MT)

|Structure-Category|Welding Category|Relation between Material of Base & Parts|Minimum-required-efficiency|Final inspection-time|
|:-------------: | :------------- | :-------------: |:-------------: | :-------------: |
| A      |Butt weld, Full penetration weld, Partial penetration weld | Same |100%|168 hours|
| A      |Butt weld, Full penetration weld, Partial penetration weld | Different |100%|168 hours|
| A      | Fillet weld|All|100%|72 hours|
| B      | Butt weld, Full penetration weld, Partial penetration weld, Fillet weld|All|100%|24 hours|
| C      | Butt weld, Full penetration weld, Partial penetration weld, Fillet weld|All|100%|Normal temperature|
| D      | Butt weld, Full penetration weld, Partial penetration weld, Fillet weld|All|N/A|N/A|

 * Ultrasonic Testing (UT) and Radiographic Testing (RT)

|Structure-Category | Welding Category | Relation between Material of Base & Parts |Minimum-required-efficiency|Final inspection-time|
| :-------------: |:-------------|:-------------:|:-------------:|:-------------:|
 | A      |Butt weld, Full penetration weld, Partial penetration weld | Same |100%|48 hours|
  | A      |Butt weld, Full penetration weld, Partial penetration weld | Different |N/A|Replacing by MT/PT in each welding layer|
 | A      | Fillet weld|All|100%|12 hours|
 | B      | Butt weld|All|100%|12 hours|
 | B      | Full penetration weld, Partial penetration weld, Fillet weld|All|N/A|N/A|
 | C      | Butt weld, Full penetration weld, Partial penetration weld, Fillet weld|All|N/A|N/A|
 | D      | Butt weld, Full penetration weld, Partial penetration weld, Fillet weld|All|N/A|N/A|

 ## Code
This pograme have a main function and three additional functions as shown below :

### Main Fuction
In the main function, the program will read the NDT Requirements List, which is in CSV format and located in the specified folder. This list currently does not include NDT methods information. The program will then proceed to write the NDT methods information into the list, updating the CSV file with the new data.

### Additional function : input_name
This function will prompt the user to input the name of the NDT Requirements List. It will then check if the file exists in the specified folder and if it is in the CSV file format.

### Additional function : mt_pt_machine
Based on the standard guidelines, function identify PT and MT information by considering the material of the base, material of parts, structure category, and welding category. PT and MT information includes the minimum-required efficiency and final inspection time. In addition, the function will also check the format of the original list. If the list is found to be in the wrong format, it will indicate errors or inconsistencies within the list.

### Additional function : ut_rt_machine
Based on the standard guidelines, function identify PT and MT information by material of base, material of parts, structure category, welding category. UT and RT information includes the minimum-required efficiency and final inspection time. In addition, the function will also check the format of the original list. If the list is found to be in the wrong format, it will indicate errors or inconsistencies within the list.

### Additional function : remarks_machine
After identifying PT/MT and UT/RT information, both of function may have remarks.This function will combine the remarks in a way that makes sense in English grammar.