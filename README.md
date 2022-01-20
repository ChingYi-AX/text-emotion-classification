# 100-lines-text-emotion-classification

- Goal of this repository:
  1. Train model on united emotion dataset (12 dataset)
  2. **ktrain** light Tensorflow keras, really easy to understand and use for beginner 
  3. Express good generalization result when evaluate on unified dataset(included 12 datasets).
  4. AWS store 

- Motivation: Emotion dataset usually not very high-quailty, different dataset is annotated via different standard, we used unified dataset, which united 12 emotion dataset, and reannotated it. emotion classification is always a challenging task in text and speech. Our model show good generalization compared to (Roman original paper)

- TODO:
- Store emtoin data in AWS(SQL), access via python script
- file strcture: 
   1. checkpoint (directory) :store checkpoint
   2. Data (directory): data_visualization.py & data_process.py & aws_script
   3. model.py: store the model architecture
   4. train_loop_pipline.py
   5. predictor.py
   6. util.py (save model, restore model)
   7. demo.ipynb
