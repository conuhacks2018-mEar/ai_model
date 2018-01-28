# ai_model
Audio classification model trained on the UrbanSound8K dataset.

### training
`
python train.py
`

### Evaluate model
`
python freeze.py \
--start_checkpoint=train/conv.ckpt-{18000} \
--clip_duration_ms=4000 \
--output_file=my_frozen_graph.pb

python label_way.py
`
