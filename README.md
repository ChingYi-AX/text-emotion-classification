100-lines-text-emotion-classification
============

<p align="left">
<a href="https://github.com/huaminghuangtw/<REPO-NAME>"><img src="https://badges.frapsoft.com/os/v3/open-source.svg?v=103" alt="Open Source Love"></a><br/>


### Introduction 
A easy-to-build emotion classification pipeline with [ktrain](https://github.com/amaiya/ktrain), which is a lightweight wrapper for the deep learning library TensorFlow Keras. We used BERT pre-trained model and trained on a unified dataset which consist of 12 emotion corporas. 

### Motivation 
  1. [ktrain](https://github.com/amaiya/ktrain) is very friendly for the beginner 
  2. Emotion datasets are usually built in different ways. This leads to several research gaps: supervised models often only use a limited set of available resources. Thus, we a promising [unified emotion corpora](https://www.ims.uni-stuttgart.de/forschung/ressourcen/korpora/unifyemotion/) from Institut für Maschinelle Sprachverarbeitung, Universität Stuttgart. The authors selected 12 emotion datasets and reannotated them. We expect to build more general model via this dataset.  
  
---

### How to use
1. Build virtual environment 
```
python3 -m venv venv
. venv/bin/activate
```
  
2. Install required package 
```
pip install -r requirements.txt
(or) pip install -e .
```
  
3. Prepare data:
 - you can find the unified emotion corpora [here](https://www.ims.uni-stuttgart.de/forschung/ressourcen/korpora/unifyemotion/)
 - The default dataset is in json or tsv format.
 - Each datapoint has following information: 'ID', 'Corpora', 'Text', 'Emotion'
  
4. Fine-tune the pre-trained model:
 - you can download the model I already fine-tuned [here](https://drive.google.com/drive/folders/1ENB_0JSyMnALlDlUkdGXR8Us_NwDiZ3v?usp=sharing)
 - make checkpoints directory in the main root and put checkpoint files inside
 - alternatively, you can fine-tune you own model 
  
---

### Result sample
 
```
Input Text: Always love 'Jeni's' ice cream🍨💓#my #favorite #icecream #ohaio #yum #delicious #happy… https://t.co/JtQ9a1Ag1z
Predicted Label --> joy /      Ground Truth Label --> joy

Input Text: @masters_say sounds like a perfect night that I miss spending with you! #imiss12303
Predicted Label --> sadness /   Ground Truth Label --> sadness

Input Text: You can't beat a bit of Division. Interzone.
Predicted Label --> noemo /     Ground Truth Label --> joy

Input Text: @JordanWooten yeah, yeah. we'll see....can't ruin Christmas.
Predicted Label --> surprise /  Ground Truth Label --> surprise

Input Text: Bon. On va tenter la cuisine avec l'huile d'arachide ...
Predicted Label --> fear /      Ground Truth Label --> fear
```
  
---

### Evaluation 
  
  <img width="680" alt="Screen Shot 2022-01-25 at 11 05 59 PM" src="https://user-images.githubusercontent.com/82449718/151067623-34570fee-cc10-4d77-8532-774623a993f2.png">

---

### To-dos
- Evaluate on individual dataset 
- Build similar pipeline for via pytorch-lightning
- More firendly to other dataset
  
 

---

### Contact
If you have any question or suggestion, feel free to contact me at haching1105@gmail.com. Contributions are also welcomed. Please open a [pull-request](https://github.com/ChingYi-AX/text-emotion-classification/compare) or an [issue](https://github.com/ChingYi-AX/text-emotion-classification/issues/new) in this repository.
 
---
### Citation
```
@inproceedings{bostan-klinger-2018-analysis,
    title = "An Analysis of Annotated Corpora for Emotion Classification in Text",
    author = "Bostan, Laura-Ana-Maria  and
      Klinger, Roman",
    booktitle = "Proceedings of the 27th International Conference on Computational Linguistics",
    month = aug,
    year = "2018",
    address = "Santa Fe, New Mexico, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/C18-1179",
}
```
