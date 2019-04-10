import torch.nn as nn
__all__ = ['vgg16_flat_02']
class VGG16(nn.Module):
	def __init__(self, num_classes=1000):
		super(VGG16, self).__init__()
		self.conv1 = nn.Conv2d(3, 23, kernel_size=3, stride=1, padding=1, bias=False)
		self.bn1 = nn.BatchNorm2d(23)
		self.conv2 = nn.Conv2d(23, 54, kernel_size=3, stride=1, padding=1, bias=False)
		self.bn2 = nn.BatchNorm2d(54)
		self.conv3 = nn.Conv2d(54, 89, kernel_size=3, stride=1, padding=1, bias=False)
		self.bn3 = nn.BatchNorm2d(89)
		self.conv4 = nn.Conv2d(89, 127, kernel_size=3, stride=1, padding=1, bias=False)
		self.bn4 = nn.BatchNorm2d(127)
		self.conv5 = nn.Conv2d(127, 231, kernel_size=3, stride=1, padding=1, bias=False)
		self.bn5 = nn.BatchNorm2d(231)
		self.conv6 = nn.Conv2d(231, 232, kernel_size=3, stride=1, padding=1, bias=False)
		self.bn6 = nn.BatchNorm2d(232)
		self.conv7 = nn.Conv2d(232, 252, kernel_size=3, stride=1, padding=1, bias=False)
		self.bn7 = nn.BatchNorm2d(252)
		self.conv8 = nn.Conv2d(252, 500, kernel_size=3, stride=1, padding=1, bias=False)
		self.bn8 = nn.BatchNorm2d(500)
		self.conv9 = nn.Conv2d(500, 505, kernel_size=3, stride=1, padding=1, bias=False)
		self.bn9 = nn.BatchNorm2d(505)
		self.conv10 = nn.Conv2d(505, 503, kernel_size=3, stride=1, padding=1, bias=False)
		self.bn10 = nn.BatchNorm2d(503)
		self.conv11 = nn.Conv2d(503, 496, kernel_size=3, stride=1, padding=1, bias=False)
		self.bn11 = nn.BatchNorm2d(496)
		self.conv12 = nn.Conv2d(496, 512, kernel_size=3, stride=1, padding=1, bias=False)
		self.bn12 = nn.BatchNorm2d(512)
		self.conv13 = nn.Conv2d(512, 512, kernel_size=3, stride=1, padding=1, bias=False)
		self.bn13 = nn.BatchNorm2d(512)
		self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
		self.avgpool = nn.AdaptiveAvgPool2d((7, 7))
		self.relu = nn.ReLU(inplace=True)
		self.fc1 = nn.Linear(25088, 2333)
		self.fc2 = nn.Linear(2333, 2805)
		self.fc3 = nn.Linear(2805, num_classes)
		self.dropout = nn.Dropout()
	def forward(self, x):
		x = self.conv1(x)
		x = self.bn1(x)
		x = self.relu(x)
		x = self.conv2(x)
		x = self.bn2(x)
		x = self.relu(x)
		x = self.pool(x)
		x = self.conv3(x)
		x = self.bn3(x)
		x = self.relu(x)
		x = self.conv4(x)
		x = self.bn4(x)
		x = self.relu(x)
		x = self.pool(x)
		x = self.conv5(x)
		x = self.bn5(x)
		x = self.relu(x)
		x = self.conv6(x)
		x = self.bn6(x)
		x = self.relu(x)
		x = self.conv7(x)
		x = self.bn7(x)
		x = self.relu(x)
		x = self.pool(x)
		x = self.conv8(x)
		x = self.bn8(x)
		x = self.relu(x)
		x = self.conv9(x)
		x = self.bn9(x)
		x = self.relu(x)
		x = self.conv10(x)
		x = self.bn10(x)
		x = self.relu(x)
		x = self.pool(x)
		x = self.conv11(x)
		x = self.bn11(x)
		x = self.relu(x)
		x = self.conv12(x)
		x = self.bn12(x)
		x = self.relu(x)
		x = self.conv13(x)
		x = self.bn13(x)
		x = self.relu(x)
		x = self.avgpool(x)
		x = x.view(x.size(0), -1)
		x = self.fc1(x)
		x = self.relu(x)
		x = self.dropout(x)
		x = self.fc2(x)
		x = self.relu(x)
		x = self.dropout(x)
		x = self.fc3(x)
		return x
def vgg16_flat_02(**kwargs):
	model = VGG16(**kwargs)
	return model
