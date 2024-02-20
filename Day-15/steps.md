## =>Data Wrangling By Applying the ```Machine Learning``` Algorithms and `Statistics`
**What is Data Wrangling?**

Data wrandling is the process of `cleaning` , `transformation, and organizing` data so that it can be used for ` analysis and visualization`. It is an important step in the data analysis process because raw data is often incomplete, inconsistent, and in an unstructured format, which can make it difficult to work with. 
- Data wrangling helps to makke the data more `consistent`, `accutate` , and `useful` for analysis and decision makin.
# Steps For Data Wrandling:
1. Gathering the data
2. Assessing the data(EDA ke saare step)
3. Cleaning the data
   1. Dealing with missing values
   2. Correcting errors in the data 
      1. Outliers Removal
         1. Visualization
         2. IQR ( Inter Quantile Range)
         3. Z- Score (Assignment)
   3. Droping duplicates (agr aik bande ka do dafa data liya ho to tab usko drop karei ge)
4. Transforming the Data
   1. Normalize the data ( Data Normalization )
      1. Min-Max normalization / scalling 
      2. Standard Scalar
      3. Log Transformation
      4. Winsorization
      5. Z-score Normalization
      6. Decimal Scaling
      7. (Har method har data ke lia theek nahi hota(`chai ke  lia cup` hota hai, `salan ke lia plate` hota hai aur, `soop ke lia bowl` hota hai)) so jis cheez ke lia jo method hota hai wahi use kana chahiye hai hamei.
      8. aik jugaar ya `tootka` Dr.Ammar ne diya hai ke uper se `IQR` aur `Visualization` ka kar lei to hamei aur koi zarurat nahi pare gi kisi dusre method ki
      9. agr ham ne baqi bhi karna hai to koi masla nahi , go for it, 10-15 methods ham nikal saktei hai but ye 6 methods important ya common hai
5. Organizing data
   1. Columns Creation
   2. Rename karei jis ki sense bane
   3. pivot table creation
6. save the data to excel or csv or any other file using pandas library
   