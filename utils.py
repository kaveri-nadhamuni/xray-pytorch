import numpy
from torch.autograd import Variable


def l2norm(input, p=2.0, dim=1, eps=1e-12):
    """
    Compute L2 norm, row-wise
    """
    #return input / input.norm(p, dim).clamp(min=eps).expand_as(input)
    #p=input.norm(p, dim).clamp(min=eps)
    copyinput = input
    #print("SIZES",input.size(),input.norm(p, dim,keepdim=True).expand_as(copyinput).size())
    return input / input.norm(p, dim,keepdim=True).clamp(min=eps).expand_as(copyinput)


def xavier_weight(tensor):
    if isinstance(tensor, Variable):
        #xavier_weight(tensor.data)
        return tensor

    nin, nout = tensor.size()[0], tensor.size()[1]
    r = numpy.sqrt(6.) / numpy.sqrt(nin + nout)
    return tensor.normal_(0, r)

