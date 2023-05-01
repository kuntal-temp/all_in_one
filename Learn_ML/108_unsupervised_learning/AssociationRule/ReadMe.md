Notes:
---
Association rule learning can be divided into three types of algorithms:
1. Apriori
2. Eclat
3. F-P Growth Algorithm


How does Association Rule Learning work?

>Association rule learning works on the concept of If and Else Statement, such as if A then B.


>Here the If element is called antecedent, and then statement is called as Consequent. These types of relationships where we can find out some association or relation between two items is known as single cardinality. It is all about creating rules, and if the number of items increases, then cardinality also increases accordingly. So, to measure the associations between thousands of data items, there are several metrics. 


These metrics are given below:

1. Support
2. Confidence
3. Lift


1. If Lift = 1: The probability of occurrence of antecedent and consequent is independent of each other.
2. Lift > 1: It determines the degree to which the two itemsets are dependent to each other.
3. Lift < 1: It tells us that one item is a substitute for other items, which means one item has a negative effect on another.


## Apriori Algorithm
>This algorithm uses frequent datasets to generate association rules. It is designed to work on the databases that contain transactions. This algorithm uses a breadth-first search and Hash Tree to calculate the itemset efficiently.
It is mainly used for market basket analysis and helps to understand the products that can be bought together. It can also be used in the healthcare field to find drug reactions for patients.


## Eclat Algorithm
>Eclat algorithm stands for Equivalence Class Transformation. This algorithm uses a depth-first search technique to find frequent itemsets in a transaction database. It performs faster execution than Apriori Algorithm.


## F-P Growth Algorithm
>The F-P growth algorithm stands for Frequent Pattern, and it is the improved version of the Apriori Algorithm. It represents the database in the form of a tree structure that is known as a frequent pattern or tree. The purpose of this frequent tree is to extract the most frequent patterns.


**Note**

>Unlike the Apriori algorithm, which is applicable with horizontal dataset, the Eclat algorithm is applicable only with a dataset in vertical dataset format.

>In the Eclat algorithm, only the support and confidence is counted as confidence. As in the case of Apriori, it is not computed. Here, the Support is nothing but the number of times an item is in a database.

>When dealing with a larger dataset, Apriori tends to shine best. Thus, the Eclat algorithm works better with small and medium datasets.

>The key takeaway here is that Eclat works well with the vertical data format. Since most datasets are in the horizontal format, to apply the Eclat algorithm, we first have to convert them to vertical format.