#Efficientnet
#ShortCut <need to import EfficientNet>
# from torchvision.models import efficientnet_v2_m, EfficientNet_V2_M_Weights


weights = EfficientNet_V2_M_Weights.IMAGENET1K_V1
model = efficientnet_v2_m(weights=weights)
classifier = model.classifier
last_layer_in_features = classifier[-1].in_features
classifier[-1] = nn.Linear(last_layer_in_features, num_classes)  # your num_classes for classification
