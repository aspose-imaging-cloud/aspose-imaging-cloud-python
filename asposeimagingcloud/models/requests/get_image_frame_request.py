# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="get_image_frame_request.py">
#   Copyright (c) 2019 Aspose Pty Ltd. All rights reserved.
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------


class GetImageFrameRequest(object):
    """
    Request model for get_image_frame operation.
    Initializes a new instance.
    :param name Filename of image.
    :param frame_id Number of a frame.
    :param new_width New width.
    :param new_height New height.
    :param x X position of start point for cropping rectangle.
    :param y Y position of start point for cropping rectangle.
    :param rect_width Width of cropping rectangle.
    :param rect_height Height of cropping rectangle.
    :param rotate_flip_method RotateFlip method (Rotate180FlipNone, Rotate180FlipX, Rotate180FlipXY, Rotate180FlipY, Rotate270FlipNone, Rotate270FlipX, Rotate270FlipXY, Rotate270FlipY, Rotate90FlipNone, Rotate90FlipX, Rotate90FlipXY, Rotate90FlipY, RotateNoneFlipNone, RotateNoneFlipX, RotateNoneFlipXY, RotateNoneFlipY). Default is RotateNoneFlipNone.
    :param save_other_frames If result will include all other frames or just a specified frame.
    :param out_path Path to updated file (if this is empty, response contains streamed image).
    :param folder Folder with image to process.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, frame_id, new_width=None, new_height=None, x=None, y=None, rect_width=None, rect_height=None, rotate_flip_method=None, save_other_frames=None, out_path=None, folder=None, storage=None):
        self.name = name
        self.frame_id = frame_id
        self.new_width = new_width
        self.new_height = new_height
        self.x = x
        self.y = y
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.rotate_flip_method = rotate_flip_method
        self.save_other_frames = save_other_frames
        self.out_path = out_path
        self.folder = folder
        self.storage = storage
