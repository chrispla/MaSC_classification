# Classification of Eisenberg and Arab Mashriq Collections

Experiments on classifying the two collections based on audio features

### Dataset 

**2766** songs (considering all excerpts with a duration of 15 seconds)

**2328** songs from the Arab Mashriq Collection

**438** songs from the Eisenberg Collection



### Preprocessing

All features were normalized before being used for classification by removing the mean and scaling to unit variance.



### Results

**6-fold cross-validation** (shuffle=True) | **R² scores**

| Classifier \ Features                                       | MFCCs (13)                                                   | Mel Spectrogram                                              |
| :---------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **MLP** <br />*(100, ), activation=’relu’*, *solver=’adam’* | *0.9674620390455532<br />0.9327548806941431<br />0.9370932754880694<br />0.9674620390455532<br />0.9696312364425163<br />0.9501084598698482* | *0.8872017353579176<br />0.8590021691973969<br />0.9023861171366594<br />0.8872017353579176<br />0.8850325379609545<br />0.8741865509761388* |
| **SVC**<br />kernel='rbf'                                   | *0.9674620390455532<br />0.9457700650759219<br />0.96529284164859<br />0.96529284164859<br />0.96529284164859<br />0.9544468546637744* | *0.8524945770065075<br />0.8221258134490239<br />0.8828633405639913<br />0.8373101952277657<br />0.8676789587852495<br />0.8720173535791758* |



**Stratified 6-fold cross-validation** | **R² scores**

| Classifier \ Features                                       | MFCCs (13)                                                   | Mel Spectrogram                                              |
| :---------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **MLP** <br />*(100, ), activation=’relu’*, *solver=’adam’* | *0.98047722* <br />*0.90455531* <br />*0.87852495* <br />*0.96095445*<br />*0.90672451* <br />*0.89154013* | *0.90455531* <br />*0.81778742* <br />*0.93275488* <br />*0.86334056* <br />*0.79826464* <br />*0.76789588* |
| **SVC**<br />kernel='rbf'                                   | *0.98481562<br />0.92841649<br />0.9132321* <br />*0.96746204<br />0.90021692<br />0.88286334* | *0.85032538<br />0.85466377* <br />*0.85032538* <br />*0.85900217* <br />*0.82863341*<br />*0.8373102* |



<em>**Note 1**: Discrepancy in float precision between Stratified and non-Stratified cross-validation scores is due to the use of the ‘model_selection.cross_val_score’ method which only works with Stratified cross-validation in the case of binary and multiclass targets. For the non-Stratified cross-validation scores a combination of lower-level methods was used.</em>

<em>**Note 2:** *While in the case of very small datasets with huge imbalances of Arab vs Eisenberg there were cases were the classifiers would either not work or have no accuracy in the non-Stratified cross-validations, this phenomenon was obviously very unlikely in the entirety of the dataset, were multiple reinitializations of the folds would have had to be performed to get folds that would be comprised of single-class targets.*</em>
