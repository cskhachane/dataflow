# Google Dataflow 

## Apache Beam Side Inputs :
Side Input is generally a small dataset (configuration parameters/lookups/stopwords).

There are 3 different types of Side Inputs that is used in Apache Beam.
1. SingleTon.py - read individual values from Pcollection
2. AsDict.py    - read values as a dictionary from Pcollection
3. AsList.py    - read values as a list from Pcollection

Code example available in the folder **Apache_Beam_SideInputs**/
  1. Beam_SideInput_SingleTon.py
  2. Beam_SideInput_AsDict.py
  3. Beam_SideInput_AsList.py
   
## Apache Beam Counts :
There are 3 different types of Counts that is used in Apache Beam.

Count.Globally()   - counting all elements in a PCollection.  
Count.PerKey()     - counting elements for each unique key in a Pcollection of keyvalues.  
Count.PerElement() - counting only unique elements in a Pcollection.  

Code example available in the folder **Apache_Beam_Count**/
  1. count_perElement.py
  2. count_perKey.py
  3. count_Globally.py

Windows:
Press Windows + . (Windows key + period) to open the emoji picker.
