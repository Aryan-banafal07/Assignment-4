# Assignment-4
Exploratory Data Analysis (EDA) Conduct an in-depth Exploratory Data Analysis on a complex dataset. Focus on understanding data distributions, identifying missing values, detecting outliers, and uncovering relationships between variables. Utilize visualizations like histograms, box plots, and heatmaps to support your findings.


# Output

Dataset Info:

 No   Column       Non-Null Count  Dtype   
---  ------       --------------  -----   
 0   survived     891 non-null    int64   
 1   pclass       891 non-null    int64   
 2   sex          891 non-null    object  
 3   age          714 non-null    float64 
 4   sibsp        891 non-null    int64   
 5   parch        891 non-null    int64   
 6   fare         891 non-null    float64 
 7   embarked     889 non-null    object  
 8   class        891 non-null    category
 9   who          891 non-null    object  
 10  adult_male   891 non-null    bool    
 11  deck         203 non-null    category
 12  embark_town  889 non-null    object  
 13  alive        891 non-null    object  
 14  alone        891 non-null    bool    
dtypes: bool(2), category(2), float64(2), int64(4), object(5)
memory usage: 80.7+ KB

Descriptive Statistics:
          survived      pclass   sex         age       sibsp       parch  \
count   891.000000  891.000000   891  714.000000  891.000000  891.000000   
unique         NaN         NaN     2         NaN         NaN         NaN   
top            NaN         NaN  male         NaN         NaN         NaN   
freq           NaN         NaN   577         NaN         NaN         NaN   
mean      0.383838    2.308642   NaN   29.699118    0.523008    0.381594   
std       0.486592    0.836071   NaN   14.526497    1.102743    0.806057   
min       0.000000    1.000000   NaN    0.420000    0.000000    0.000000   
25%       0.000000    2.000000   NaN   20.125000    0.000000    0.000000   
50%       0.000000    3.000000   NaN   28.000000    0.000000    0.000000   
75%       1.000000    3.000000   NaN   38.000000    1.000000    0.000000   
max       1.000000    3.000000   NaN   80.000000    8.000000    6.000000   

              fare embarked  class  who adult_male deck  embark_town alive  \
count   891.000000      889    891  891        891  203          889   891   
unique         NaN        3      3    3          2    7            3     2   
top            NaN        S  Third  man       True    C  Southampton    no   
freq           NaN      644    491  537        537   59          644   549   
mean     32.204208      NaN    NaN  NaN        NaN  NaN          NaN   NaN   
std      49.693429      NaN    NaN  NaN        NaN  NaN          NaN   NaN   
min       0.000000      NaN    NaN  NaN        NaN  NaN          NaN   NaN   
25%       7.910400      NaN    NaN  NaN        NaN  NaN          NaN   NaN   
50%      14.454200      NaN    NaN  NaN        NaN  NaN          NaN   NaN   
75%      31.000000      NaN    NaN  NaN        NaN  NaN          NaN   NaN   
max     512.329200      NaN    NaN  NaN        NaN  NaN          NaN   NaN   


![image](https://github.com/user-attachments/assets/fd9aad5a-da29-4f97-9159-678d71aff56f)

![image](https://github.com/user-attachments/assets/d4fc07cc-bdd8-4643-ad2b-88429b8ba90a)

![image](https://github.com/user-attachments/assets/0e0c5460-3682-4a8c-80b1-94c63a97537b)

![image](https://github.com/user-attachments/assets/9b2b9679-ab78-40bd-91bc-5353c77e564f)

![image](https://github.com/user-attachments/assets/7f989814-26d9-49e4-aff0-e9b1cac05da0)

![image](https://github.com/user-attachments/assets/a63be8f4-3711-48db-a4a4-ac7ee9482766)

![image](https://github.com/user-attachments/assets/7390db31-cef9-46c9-98f5-3eb2f3ea959e)

![image](https://github.com/user-attachments/assets/fef83d8f-19d3-4bb5-aa41-69dfa383dc40)

![image](https://github.com/user-attachments/assets/aa1ec1db-e325-4851-85b3-cac87fd6d81b)

![image](https://github.com/user-attachments/assets/a3006921-25f8-4bfe-bb1e-28bf1202a1ba)

![image](https://github.com/user-attachments/assets/71c5d018-cd95-4d73-b58d-9a50e6175356)

![image](https://github.com/user-attachments/assets/5bc5c926-82de-4da0-bdb2-4c689b644649)

![image](https://github.com/user-attachments/assets/06d07ec0-19f0-4d75-b841-9eb0d19509c1)


Encoded Data Preview:
   survived  pclass  sex   age  sibsp  parch     fare  embarked  alone
0         0       3    0  22.0      1      0   7.2500       0.0  False
1         1       1    1  38.0      1      0  71.2833       1.0  False
2         1       3    1  26.0      0      0   7.9250       0.0   True
3         1       1    1  35.0      1      0  53.1000       0.0  False
4         0       3    0  35.0      0      0   8.0500       0.0   True
