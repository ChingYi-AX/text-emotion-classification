# 100-lines-text-emotion-classification
- Goal of this repository:
  1. Train model on united emotion dataset (12 dataset)
  2. light Tensorflow keras, really easy to understand and use for beginner 
  3. Very good result compared to the exist text emotion classification
  4. AWS store 
- Motivation: Emotion dataset usually not very high-quailty. emotion classification is always a challenging task in text and speech.
- Store emtoinn data in AWS(SQL), access via python script
- file strcture: 
   1. checkpoint (directory) :store checkpoint
   2. Data (directory): data_visualization.py & data_process.py & aws_script
   3. model.py: store the model architecture
   4. train_loop_pipline.py
   5. predictor.py
   6. util.py (save model, restore model)
   7. demo.ipynb
