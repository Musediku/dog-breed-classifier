import ast
from PIL import Image
import torchvision.transforms as transforms
from torch import __version__
import torchvision.models as models

# Use the new 'weights' argument instead of 'pretrained'
from torchvision.models import ResNet18_Weights, AlexNet_Weights, VGG16_Weights

resnet18 = models.resnet18(weights=ResNet18_Weights.DEFAULT)
alexnet = models.alexnet(weights=AlexNet_Weights.DEFAULT)
vgg16 = models.vgg16(weights=VGG16_Weights.DEFAULT)

models_dict = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}

# Obtain ImageNet labels
with open('imagenet1000_clsid_to_human.txt') as f:
    imagenet_classes_dict = ast.literal_eval(f.read())

def classifier(img_path, model_name):
    # load the image
    img_pil = Image.open(img_path)

    # define transforms
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    # preprocess the image
    img_tensor = preprocess(img_pil)
    
    # add batch dimension
    img_tensor.unsqueeze_(0)
    
    # make tensor not require gradients (for inference)
    pytorch_ver = __version__.split('.')
    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:
        img_tensor.requires_grad_(False)
    else:
        from torch.autograd import Variable
        img_tensor = Variable(img_tensor, volatile=True)
    
    # select model
    model = models_dict[model_name]
    model.eval()  # set to evaluation mode
    
    # get model output
    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:
        output = model(img_tensor)
    else:
        output = model(img_tensor)  # older versions handle Variable differently

    # return predicted label
    pred_idx = output.data.numpy().argmax()
    return imagenet_classes_dict[pred_idx]
