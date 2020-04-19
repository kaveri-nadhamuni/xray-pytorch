Based on code from https://github.com/linxd5/VSE_Pytorch, pytorch code for the image-sentence ranking methods from *[Unifying Visual-Semantic Embeddings with Multimodal Neural Language Models](https://arxiv.org/abs/1411.2539)* (Kiros,Salakhutdinov, Zemel, 2014).

Modified image processing pipeline to get xray representations. Used the ranking and retrieval image-captioning pipeline but replaced image processing CNN with kaggle X-ray classification model. xray model, images and captions stores in vse/xray and data/xray. 
