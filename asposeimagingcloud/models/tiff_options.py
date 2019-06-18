# coding: utf-8
# -----------------------------------------------------------------------------
# <copyright company="Aspose" file="TiffOptions.py">
#   Copyright (c) 2019 Aspose Pty Ltd. All rights reserved.
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a
#  copy  of this software and associated documentation files (the "Software"),
#  to deal  in the Software without restriction, including without limitation
#  the rights  to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell  copies of the Software, and to permit persons to whom the
#  Software is  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM,  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------
import pprint
import re
import six


class TiffOptions(object):
    """Represents options for TIFF frame.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'is_valid': 'bool',
        'artist': 'str',
        'byte_order': 'str',
        'bits_per_sample': 'list[int]',
        'compression': 'str',
        'copyright': 'str',
        'color_map': 'list[int]',
        'date_time': 'str',
        'document_name': 'str',
        'alpha_storage': 'str',
        'fill_order': 'str',
        'half_tone_hints': 'list[int]',
        'image_description': 'str',
        'ink_names': 'str',
        'scanner_manufacturer': 'str',
        'max_sample_value': 'list[int]',
        'min_sample_value': 'list[int]',
        'scanner_model': 'str',
        'page_name': 'str',
        'orientation': 'str',
        'page_number': 'list[int]',
        'photometric': 'str',
        'planar_configuration': 'str',
        'resolution_unit': 'str',
        'rows_per_strip': 'int',
        'sample_format': 'list[str]',
        'samples_per_pixel': 'int',
        'smax_sample_value': 'list[int]',
        'smin_sample_value': 'list[int]',
        'software_type': 'str',
        'strip_byte_counts': 'list[int]',
        'strip_offsets': 'list[int]',
        'sub_file_type': 'str',
        'target_printer': 'str',
        'threshholding': 'str',
        'total_pages': 'int',
        'xposition': 'float',
        'xresolution': 'float',
        'yposition': 'float',
        'yresolution': 'float',
        'fax_t4_options': 'str',
        'predictor': 'str',
        'image_length': 'int',
        'image_width': 'int',
        'valid_tag_count': 'int',
        'bits_per_pixel': 'int'
    }

    attribute_map = {
        'is_valid': 'IsValid',
        'artist': 'Artist',
        'byte_order': 'ByteOrder',
        'bits_per_sample': 'BitsPerSample',
        'compression': 'Compression',
        'copyright': 'Copyright',
        'color_map': 'ColorMap',
        'date_time': 'DateTime',
        'document_name': 'DocumentName',
        'alpha_storage': 'AlphaStorage',
        'fill_order': 'FillOrder',
        'half_tone_hints': 'HalfToneHints',
        'image_description': 'ImageDescription',
        'ink_names': 'InkNames',
        'scanner_manufacturer': 'ScannerManufacturer',
        'max_sample_value': 'MaxSampleValue',
        'min_sample_value': 'MinSampleValue',
        'scanner_model': 'ScannerModel',
        'page_name': 'PageName',
        'orientation': 'Orientation',
        'page_number': 'PageNumber',
        'photometric': 'Photometric',
        'planar_configuration': 'PlanarConfiguration',
        'resolution_unit': 'ResolutionUnit',
        'rows_per_strip': 'RowsPerStrip',
        'sample_format': 'SampleFormat',
        'samples_per_pixel': 'SamplesPerPixel',
        'smax_sample_value': 'SmaxSampleValue',
        'smin_sample_value': 'SminSampleValue',
        'software_type': 'SoftwareType',
        'strip_byte_counts': 'StripByteCounts',
        'strip_offsets': 'StripOffsets',
        'sub_file_type': 'SubFileType',
        'target_printer': 'TargetPrinter',
        'threshholding': 'Threshholding',
        'total_pages': 'TotalPages',
        'xposition': 'Xposition',
        'xresolution': 'Xresolution',
        'yposition': 'Yposition',
        'yresolution': 'Yresolution',
        'fax_t4_options': 'FaxT4Options',
        'predictor': 'Predictor',
        'image_length': 'ImageLength',
        'image_width': 'ImageWidth',
        'valid_tag_count': 'ValidTagCount',
        'bits_per_pixel': 'BitsPerPixel'
    }

    def __init__(self, is_valid=None, artist=None, byte_order=None, bits_per_sample=None, compression=None, copyright=None, color_map=None, date_time=None, document_name=None, alpha_storage=None, fill_order=None, half_tone_hints=None, image_description=None, ink_names=None, scanner_manufacturer=None, max_sample_value=None, min_sample_value=None, scanner_model=None, page_name=None, orientation=None, page_number=None, photometric=None, planar_configuration=None, resolution_unit=None, rows_per_strip=None, sample_format=None, samples_per_pixel=None, smax_sample_value=None, smin_sample_value=None, software_type=None, strip_byte_counts=None, strip_offsets=None, sub_file_type=None, target_printer=None, threshholding=None, total_pages=None, xposition=None, xresolution=None, yposition=None, yresolution=None, fax_t4_options=None, predictor=None, image_length=None, image_width=None, valid_tag_count=None, bits_per_pixel=None):
        """TiffOptions - a model defined in Swagger"""

        self._is_valid = None
        self._artist = None
        self._byte_order = None
        self._bits_per_sample = None
        self._compression = None
        self._copyright = None
        self._color_map = None
        self._date_time = None
        self._document_name = None
        self._alpha_storage = None
        self._fill_order = None
        self._half_tone_hints = None
        self._image_description = None
        self._ink_names = None
        self._scanner_manufacturer = None
        self._max_sample_value = None
        self._min_sample_value = None
        self._scanner_model = None
        self._page_name = None
        self._orientation = None
        self._page_number = None
        self._photometric = None
        self._planar_configuration = None
        self._resolution_unit = None
        self._rows_per_strip = None
        self._sample_format = None
        self._samples_per_pixel = None
        self._smax_sample_value = None
        self._smin_sample_value = None
        self._software_type = None
        self._strip_byte_counts = None
        self._strip_offsets = None
        self._sub_file_type = None
        self._target_printer = None
        self._threshholding = None
        self._total_pages = None
        self._xposition = None
        self._xresolution = None
        self._yposition = None
        self._yresolution = None
        self._fax_t4_options = None
        self._predictor = None
        self._image_length = None
        self._image_width = None
        self._valid_tag_count = None
        self._bits_per_pixel = None
        self.discriminator = None

        if is_valid is not None:
            self.is_valid = is_valid
        if artist is not None:
            self.artist = artist
        if byte_order is not None:
            self.byte_order = byte_order
        if bits_per_sample is not None:
            self.bits_per_sample = bits_per_sample
        if compression is not None:
            self.compression = compression
        if copyright is not None:
            self.copyright = copyright
        if color_map is not None:
            self.color_map = color_map
        if date_time is not None:
            self.date_time = date_time
        if document_name is not None:
            self.document_name = document_name
        if alpha_storage is not None:
            self.alpha_storage = alpha_storage
        if fill_order is not None:
            self.fill_order = fill_order
        if half_tone_hints is not None:
            self.half_tone_hints = half_tone_hints
        if image_description is not None:
            self.image_description = image_description
        if ink_names is not None:
            self.ink_names = ink_names
        if scanner_manufacturer is not None:
            self.scanner_manufacturer = scanner_manufacturer
        if max_sample_value is not None:
            self.max_sample_value = max_sample_value
        if min_sample_value is not None:
            self.min_sample_value = min_sample_value
        if scanner_model is not None:
            self.scanner_model = scanner_model
        if page_name is not None:
            self.page_name = page_name
        if orientation is not None:
            self.orientation = orientation
        if page_number is not None:
            self.page_number = page_number
        if photometric is not None:
            self.photometric = photometric
        if planar_configuration is not None:
            self.planar_configuration = planar_configuration
        if resolution_unit is not None:
            self.resolution_unit = resolution_unit
        if rows_per_strip is not None:
            self.rows_per_strip = rows_per_strip
        if sample_format is not None:
            self.sample_format = sample_format
        if samples_per_pixel is not None:
            self.samples_per_pixel = samples_per_pixel
        if smax_sample_value is not None:
            self.smax_sample_value = smax_sample_value
        if smin_sample_value is not None:
            self.smin_sample_value = smin_sample_value
        if software_type is not None:
            self.software_type = software_type
        if strip_byte_counts is not None:
            self.strip_byte_counts = strip_byte_counts
        if strip_offsets is not None:
            self.strip_offsets = strip_offsets
        if sub_file_type is not None:
            self.sub_file_type = sub_file_type
        if target_printer is not None:
            self.target_printer = target_printer
        if threshholding is not None:
            self.threshholding = threshholding
        if total_pages is not None:
            self.total_pages = total_pages
        if xposition is not None:
            self.xposition = xposition
        if xresolution is not None:
            self.xresolution = xresolution
        if yposition is not None:
            self.yposition = yposition
        if yresolution is not None:
            self.yresolution = yresolution
        if fax_t4_options is not None:
            self.fax_t4_options = fax_t4_options
        if predictor is not None:
            self.predictor = predictor
        if image_length is not None:
            self.image_length = image_length
        if image_width is not None:
            self.image_width = image_width
        if valid_tag_count is not None:
            self.valid_tag_count = valid_tag_count
        if bits_per_pixel is not None:
            self.bits_per_pixel = bits_per_pixel

    @property
    def is_valid(self):
        """Gets the is_valid of this TiffOptions.

        Gets or sets a value indicating whether TIFF image has valid data.

        :return: The is_valid of this TiffOptions.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this TiffOptions.

        Gets or sets a value indicating whether TIFF image has valid data.

        :param is_valid: The is_valid of this TiffOptions.
        :type: bool
        """
        if is_valid is None:
            raise ValueError("Invalid value for `is_valid`, must not be `None`")
        self._is_valid = is_valid

    @property
    def artist(self):
        """Gets the artist of this TiffOptions.

        Gets or sets the artist.

        :return: The artist of this TiffOptions.
        :rtype: str
        """
        return self._artist

    @artist.setter
    def artist(self, artist):
        """Sets the artist of this TiffOptions.

        Gets or sets the artist.

        :param artist: The artist of this TiffOptions.
        :type: str
        """
        self._artist = artist

    @property
    def byte_order(self):
        """Gets the byte_order of this TiffOptions.

        Gets or sets the byte order.

        :return: The byte_order of this TiffOptions.
        :rtype: str
        """
        return self._byte_order

    @byte_order.setter
    def byte_order(self, byte_order):
        """Sets the byte_order of this TiffOptions.

        Gets or sets the byte order.

        :param byte_order: The byte_order of this TiffOptions.
        :type: str
        """
        self._byte_order = byte_order

    @property
    def bits_per_sample(self):
        """Gets the bits_per_sample of this TiffOptions.

        Gets or sets the bits per sample.

        :return: The bits_per_sample of this TiffOptions.
        :rtype: list[int]
        """
        return self._bits_per_sample

    @bits_per_sample.setter
    def bits_per_sample(self, bits_per_sample):
        """Sets the bits_per_sample of this TiffOptions.

        Gets or sets the bits per sample.

        :param bits_per_sample: The bits_per_sample of this TiffOptions.
        :type: list[int]
        """
        self._bits_per_sample = bits_per_sample

    @property
    def compression(self):
        """Gets the compression of this TiffOptions.

        Gets or sets the compression.

        :return: The compression of this TiffOptions.
        :rtype: str
        """
        return self._compression

    @compression.setter
    def compression(self, compression):
        """Sets the compression of this TiffOptions.

        Gets or sets the compression.

        :param compression: The compression of this TiffOptions.
        :type: str
        """
        self._compression = compression

    @property
    def copyright(self):
        """Gets the copyright of this TiffOptions.

        Gets or sets the copyright info.

        :return: The copyright of this TiffOptions.
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this TiffOptions.

        Gets or sets the copyright info.

        :param copyright: The copyright of this TiffOptions.
        :type: str
        """
        self._copyright = copyright

    @property
    def color_map(self):
        """Gets the color_map of this TiffOptions.

        Gets or sets the color map.

        :return: The color_map of this TiffOptions.
        :rtype: list[int]
        """
        return self._color_map

    @color_map.setter
    def color_map(self, color_map):
        """Sets the color_map of this TiffOptions.

        Gets or sets the color map.

        :param color_map: The color_map of this TiffOptions.
        :type: list[int]
        """
        self._color_map = color_map

    @property
    def date_time(self):
        """Gets the date_time of this TiffOptions.

        Gets or sets the date and time.

        :return: The date_time of this TiffOptions.
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this TiffOptions.

        Gets or sets the date and time.

        :param date_time: The date_time of this TiffOptions.
        :type: str
        """
        self._date_time = date_time

    @property
    def document_name(self):
        """Gets the document_name of this TiffOptions.

        Gets or sets the document name.

        :return: The document_name of this TiffOptions.
        :rtype: str
        """
        return self._document_name

    @document_name.setter
    def document_name(self, document_name):
        """Sets the document_name of this TiffOptions.

        Gets or sets the document name.

        :param document_name: The document_name of this TiffOptions.
        :type: str
        """
        self._document_name = document_name

    @property
    def alpha_storage(self):
        """Gets the alpha_storage of this TiffOptions.

        Gets or sets the alpha storage.

        :return: The alpha_storage of this TiffOptions.
        :rtype: str
        """
        return self._alpha_storage

    @alpha_storage.setter
    def alpha_storage(self, alpha_storage):
        """Sets the alpha_storage of this TiffOptions.

        Gets or sets the alpha storage.

        :param alpha_storage: The alpha_storage of this TiffOptions.
        :type: str
        """
        self._alpha_storage = alpha_storage

    @property
    def fill_order(self):
        """Gets the fill_order of this TiffOptions.

        Gets or sets the fill order.

        :return: The fill_order of this TiffOptions.
        :rtype: str
        """
        return self._fill_order

    @fill_order.setter
    def fill_order(self, fill_order):
        """Sets the fill_order of this TiffOptions.

        Gets or sets the fill order.

        :param fill_order: The fill_order of this TiffOptions.
        :type: str
        """
        self._fill_order = fill_order

    @property
    def half_tone_hints(self):
        """Gets the half_tone_hints of this TiffOptions.

        Gets or sets the half-tone hints.

        :return: The half_tone_hints of this TiffOptions.
        :rtype: list[int]
        """
        return self._half_tone_hints

    @half_tone_hints.setter
    def half_tone_hints(self, half_tone_hints):
        """Sets the half_tone_hints of this TiffOptions.

        Gets or sets the half-tone hints.

        :param half_tone_hints: The half_tone_hints of this TiffOptions.
        :type: list[int]
        """
        self._half_tone_hints = half_tone_hints

    @property
    def image_description(self):
        """Gets the image_description of this TiffOptions.

        Gets or sets the image description.

        :return: The image_description of this TiffOptions.
        :rtype: str
        """
        return self._image_description

    @image_description.setter
    def image_description(self, image_description):
        """Sets the image_description of this TiffOptions.

        Gets or sets the image description.

        :param image_description: The image_description of this TiffOptions.
        :type: str
        """
        self._image_description = image_description

    @property
    def ink_names(self):
        """Gets the ink_names of this TiffOptions.

        Gets or sets the ink names.

        :return: The ink_names of this TiffOptions.
        :rtype: str
        """
        return self._ink_names

    @ink_names.setter
    def ink_names(self, ink_names):
        """Sets the ink_names of this TiffOptions.

        Gets or sets the ink names.

        :param ink_names: The ink_names of this TiffOptions.
        :type: str
        """
        self._ink_names = ink_names

    @property
    def scanner_manufacturer(self):
        """Gets the scanner_manufacturer of this TiffOptions.

        Gets or sets the scanner manufacturer.

        :return: The scanner_manufacturer of this TiffOptions.
        :rtype: str
        """
        return self._scanner_manufacturer

    @scanner_manufacturer.setter
    def scanner_manufacturer(self, scanner_manufacturer):
        """Sets the scanner_manufacturer of this TiffOptions.

        Gets or sets the scanner manufacturer.

        :param scanner_manufacturer: The scanner_manufacturer of this TiffOptions.
        :type: str
        """
        self._scanner_manufacturer = scanner_manufacturer

    @property
    def max_sample_value(self):
        """Gets the max_sample_value of this TiffOptions.

        Gets or sets the max sample value.

        :return: The max_sample_value of this TiffOptions.
        :rtype: list[int]
        """
        return self._max_sample_value

    @max_sample_value.setter
    def max_sample_value(self, max_sample_value):
        """Sets the max_sample_value of this TiffOptions.

        Gets or sets the max sample value.

        :param max_sample_value: The max_sample_value of this TiffOptions.
        :type: list[int]
        """
        self._max_sample_value = max_sample_value

    @property
    def min_sample_value(self):
        """Gets the min_sample_value of this TiffOptions.

        Gets or sets the min sample value.

        :return: The min_sample_value of this TiffOptions.
        :rtype: list[int]
        """
        return self._min_sample_value

    @min_sample_value.setter
    def min_sample_value(self, min_sample_value):
        """Sets the min_sample_value of this TiffOptions.

        Gets or sets the min sample value.

        :param min_sample_value: The min_sample_value of this TiffOptions.
        :type: list[int]
        """
        self._min_sample_value = min_sample_value

    @property
    def scanner_model(self):
        """Gets the scanner_model of this TiffOptions.

        Gets or sets the scanner model.

        :return: The scanner_model of this TiffOptions.
        :rtype: str
        """
        return self._scanner_model

    @scanner_model.setter
    def scanner_model(self, scanner_model):
        """Sets the scanner_model of this TiffOptions.

        Gets or sets the scanner model.

        :param scanner_model: The scanner_model of this TiffOptions.
        :type: str
        """
        self._scanner_model = scanner_model

    @property
    def page_name(self):
        """Gets the page_name of this TiffOptions.

        Gets or sets the page name.

        :return: The page_name of this TiffOptions.
        :rtype: str
        """
        return self._page_name

    @page_name.setter
    def page_name(self, page_name):
        """Sets the page_name of this TiffOptions.

        Gets or sets the page name.

        :param page_name: The page_name of this TiffOptions.
        :type: str
        """
        self._page_name = page_name

    @property
    def orientation(self):
        """Gets the orientation of this TiffOptions.

        Gets or sets the orientation.

        :return: The orientation of this TiffOptions.
        :rtype: str
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this TiffOptions.

        Gets or sets the orientation.

        :param orientation: The orientation of this TiffOptions.
        :type: str
        """
        self._orientation = orientation

    @property
    def page_number(self):
        """Gets the page_number of this TiffOptions.

        Gets or sets the page number.

        :return: The page_number of this TiffOptions.
        :rtype: list[int]
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this TiffOptions.

        Gets or sets the page number.

        :param page_number: The page_number of this TiffOptions.
        :type: list[int]
        """
        self._page_number = page_number

    @property
    def photometric(self):
        """Gets the photometric of this TiffOptions.

        Gets or sets the photometric interpretation.

        :return: The photometric of this TiffOptions.
        :rtype: str
        """
        return self._photometric

    @photometric.setter
    def photometric(self, photometric):
        """Sets the photometric of this TiffOptions.

        Gets or sets the photometric interpretation.

        :param photometric: The photometric of this TiffOptions.
        :type: str
        """
        self._photometric = photometric

    @property
    def planar_configuration(self):
        """Gets the planar_configuration of this TiffOptions.

        Gets or sets the planar configuration.

        :return: The planar_configuration of this TiffOptions.
        :rtype: str
        """
        return self._planar_configuration

    @planar_configuration.setter
    def planar_configuration(self, planar_configuration):
        """Sets the planar_configuration of this TiffOptions.

        Gets or sets the planar configuration.

        :param planar_configuration: The planar_configuration of this TiffOptions.
        :type: str
        """
        self._planar_configuration = planar_configuration

    @property
    def resolution_unit(self):
        """Gets the resolution_unit of this TiffOptions.

        Gets or sets the resolution unit.

        :return: The resolution_unit of this TiffOptions.
        :rtype: str
        """
        return self._resolution_unit

    @resolution_unit.setter
    def resolution_unit(self, resolution_unit):
        """Sets the resolution_unit of this TiffOptions.

        Gets or sets the resolution unit.

        :param resolution_unit: The resolution_unit of this TiffOptions.
        :type: str
        """
        self._resolution_unit = resolution_unit

    @property
    def rows_per_strip(self):
        """Gets the rows_per_strip of this TiffOptions.

        Gets or sets the rows per strip.

        :return: The rows_per_strip of this TiffOptions.
        :rtype: int
        """
        return self._rows_per_strip

    @rows_per_strip.setter
    def rows_per_strip(self, rows_per_strip):
        """Sets the rows_per_strip of this TiffOptions.

        Gets or sets the rows per strip.

        :param rows_per_strip: The rows_per_strip of this TiffOptions.
        :type: int
        """
        if rows_per_strip is None:
            raise ValueError("Invalid value for `rows_per_strip`, must not be `None`")
        self._rows_per_strip = rows_per_strip

    @property
    def sample_format(self):
        """Gets the sample_format of this TiffOptions.

        Gets or sets the sample format.

        :return: The sample_format of this TiffOptions.
        :rtype: list[str]
        """
        return self._sample_format

    @sample_format.setter
    def sample_format(self, sample_format):
        """Sets the sample_format of this TiffOptions.

        Gets or sets the sample format.

        :param sample_format: The sample_format of this TiffOptions.
        :type: list[str]
        """
        self._sample_format = sample_format

    @property
    def samples_per_pixel(self):
        """Gets the samples_per_pixel of this TiffOptions.

        Gets or sets the samples per pixel.

        :return: The samples_per_pixel of this TiffOptions.
        :rtype: int
        """
        return self._samples_per_pixel

    @samples_per_pixel.setter
    def samples_per_pixel(self, samples_per_pixel):
        """Sets the samples_per_pixel of this TiffOptions.

        Gets or sets the samples per pixel.

        :param samples_per_pixel: The samples_per_pixel of this TiffOptions.
        :type: int
        """
        if samples_per_pixel is None:
            raise ValueError("Invalid value for `samples_per_pixel`, must not be `None`")
        self._samples_per_pixel = samples_per_pixel

    @property
    def smax_sample_value(self):
        """Gets the smax_sample_value of this TiffOptions.

        Gets or sets the Smax sample value.

        :return: The smax_sample_value of this TiffOptions.
        :rtype: list[int]
        """
        return self._smax_sample_value

    @smax_sample_value.setter
    def smax_sample_value(self, smax_sample_value):
        """Sets the smax_sample_value of this TiffOptions.

        Gets or sets the Smax sample value.

        :param smax_sample_value: The smax_sample_value of this TiffOptions.
        :type: list[int]
        """
        self._smax_sample_value = smax_sample_value

    @property
    def smin_sample_value(self):
        """Gets the smin_sample_value of this TiffOptions.

        Gets or sets the Smin sample value.

        :return: The smin_sample_value of this TiffOptions.
        :rtype: list[int]
        """
        return self._smin_sample_value

    @smin_sample_value.setter
    def smin_sample_value(self, smin_sample_value):
        """Sets the smin_sample_value of this TiffOptions.

        Gets or sets the Smin sample value.

        :param smin_sample_value: The smin_sample_value of this TiffOptions.
        :type: list[int]
        """
        self._smin_sample_value = smin_sample_value

    @property
    def software_type(self):
        """Gets the software_type of this TiffOptions.

        Gets or sets the software type.

        :return: The software_type of this TiffOptions.
        :rtype: str
        """
        return self._software_type

    @software_type.setter
    def software_type(self, software_type):
        """Sets the software_type of this TiffOptions.

        Gets or sets the software type.

        :param software_type: The software_type of this TiffOptions.
        :type: str
        """
        self._software_type = software_type

    @property
    def strip_byte_counts(self):
        """Gets the strip_byte_counts of this TiffOptions.

        Gets or sets the strip byte counts.

        :return: The strip_byte_counts of this TiffOptions.
        :rtype: list[int]
        """
        return self._strip_byte_counts

    @strip_byte_counts.setter
    def strip_byte_counts(self, strip_byte_counts):
        """Sets the strip_byte_counts of this TiffOptions.

        Gets or sets the strip byte counts.

        :param strip_byte_counts: The strip_byte_counts of this TiffOptions.
        :type: list[int]
        """
        self._strip_byte_counts = strip_byte_counts

    @property
    def strip_offsets(self):
        """Gets the strip_offsets of this TiffOptions.

        Gets or sets the strip offsets.

        :return: The strip_offsets of this TiffOptions.
        :rtype: list[int]
        """
        return self._strip_offsets

    @strip_offsets.setter
    def strip_offsets(self, strip_offsets):
        """Sets the strip_offsets of this TiffOptions.

        Gets or sets the strip offsets.

        :param strip_offsets: The strip_offsets of this TiffOptions.
        :type: list[int]
        """
        self._strip_offsets = strip_offsets

    @property
    def sub_file_type(self):
        """Gets the sub_file_type of this TiffOptions.

        Gets or sets the subfile type.

        :return: The sub_file_type of this TiffOptions.
        :rtype: str
        """
        return self._sub_file_type

    @sub_file_type.setter
    def sub_file_type(self, sub_file_type):
        """Sets the sub_file_type of this TiffOptions.

        Gets or sets the subfile type.

        :param sub_file_type: The sub_file_type of this TiffOptions.
        :type: str
        """
        self._sub_file_type = sub_file_type

    @property
    def target_printer(self):
        """Gets the target_printer of this TiffOptions.

        Gets or sets the target printer.

        :return: The target_printer of this TiffOptions.
        :rtype: str
        """
        return self._target_printer

    @target_printer.setter
    def target_printer(self, target_printer):
        """Sets the target_printer of this TiffOptions.

        Gets or sets the target printer.

        :param target_printer: The target_printer of this TiffOptions.
        :type: str
        """
        self._target_printer = target_printer

    @property
    def threshholding(self):
        """Gets the threshholding of this TiffOptions.

        Gets or sets the threshholding.

        :return: The threshholding of this TiffOptions.
        :rtype: str
        """
        return self._threshholding

    @threshholding.setter
    def threshholding(self, threshholding):
        """Sets the threshholding of this TiffOptions.

        Gets or sets the threshholding.

        :param threshholding: The threshholding of this TiffOptions.
        :type: str
        """
        self._threshholding = threshholding

    @property
    def total_pages(self):
        """Gets the total_pages of this TiffOptions.

        Gets or sets the total pages count.

        :return: The total_pages of this TiffOptions.
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this TiffOptions.

        Gets or sets the total pages count.

        :param total_pages: The total_pages of this TiffOptions.
        :type: int
        """
        if total_pages is None:
            raise ValueError("Invalid value for `total_pages`, must not be `None`")
        self._total_pages = total_pages

    @property
    def xposition(self):
        """Gets the xposition of this TiffOptions.

        Gets or sets the X position.

        :return: The xposition of this TiffOptions.
        :rtype: float
        """
        return self._xposition

    @xposition.setter
    def xposition(self, xposition):
        """Sets the xposition of this TiffOptions.

        Gets or sets the X position.

        :param xposition: The xposition of this TiffOptions.
        :type: float
        """
        if xposition is None:
            raise ValueError("Invalid value for `xposition`, must not be `None`")
        self._xposition = xposition

    @property
    def xresolution(self):
        """Gets the xresolution of this TiffOptions.

        Gets or sets the X resolution.

        :return: The xresolution of this TiffOptions.
        :rtype: float
        """
        return self._xresolution

    @xresolution.setter
    def xresolution(self, xresolution):
        """Sets the xresolution of this TiffOptions.

        Gets or sets the X resolution.

        :param xresolution: The xresolution of this TiffOptions.
        :type: float
        """
        if xresolution is None:
            raise ValueError("Invalid value for `xresolution`, must not be `None`")
        self._xresolution = xresolution

    @property
    def yposition(self):
        """Gets the yposition of this TiffOptions.

        Gets or sets the Y position.

        :return: The yposition of this TiffOptions.
        :rtype: float
        """
        return self._yposition

    @yposition.setter
    def yposition(self, yposition):
        """Sets the yposition of this TiffOptions.

        Gets or sets the Y position.

        :param yposition: The yposition of this TiffOptions.
        :type: float
        """
        if yposition is None:
            raise ValueError("Invalid value for `yposition`, must not be `None`")
        self._yposition = yposition

    @property
    def yresolution(self):
        """Gets the yresolution of this TiffOptions.

        Gets or sets the Y resolution.

        :return: The yresolution of this TiffOptions.
        :rtype: float
        """
        return self._yresolution

    @yresolution.setter
    def yresolution(self, yresolution):
        """Sets the yresolution of this TiffOptions.

        Gets or sets the Y resolution.

        :param yresolution: The yresolution of this TiffOptions.
        :type: float
        """
        if yresolution is None:
            raise ValueError("Invalid value for `yresolution`, must not be `None`")
        self._yresolution = yresolution

    @property
    def fax_t4_options(self):
        """Gets the fax_t4_options of this TiffOptions.

        Gets or sets the FaxT4 Options.

        :return: The fax_t4_options of this TiffOptions.
        :rtype: str
        """
        return self._fax_t4_options

    @fax_t4_options.setter
    def fax_t4_options(self, fax_t4_options):
        """Sets the fax_t4_options of this TiffOptions.

        Gets or sets the FaxT4 Options.

        :param fax_t4_options: The fax_t4_options of this TiffOptions.
        :type: str
        """
        self._fax_t4_options = fax_t4_options

    @property
    def predictor(self):
        """Gets the predictor of this TiffOptions.

        Gets or sets the predictor (a mathematical operator that is applied to the image data before an encoding scheme is applied).

        :return: The predictor of this TiffOptions.
        :rtype: str
        """
        return self._predictor

    @predictor.setter
    def predictor(self, predictor):
        """Sets the predictor of this TiffOptions.

        Gets or sets the predictor (a mathematical operator that is applied to the image data before an encoding scheme is applied).

        :param predictor: The predictor of this TiffOptions.
        :type: str
        """
        self._predictor = predictor

    @property
    def image_length(self):
        """Gets the image_length of this TiffOptions.

        Gets or sets the image length.

        :return: The image_length of this TiffOptions.
        :rtype: int
        """
        return self._image_length

    @image_length.setter
    def image_length(self, image_length):
        """Sets the image_length of this TiffOptions.

        Gets or sets the image length.

        :param image_length: The image_length of this TiffOptions.
        :type: int
        """
        if image_length is None:
            raise ValueError("Invalid value for `image_length`, must not be `None`")
        self._image_length = image_length

    @property
    def image_width(self):
        """Gets the image_width of this TiffOptions.

        Gets or sets the image width.

        :return: The image_width of this TiffOptions.
        :rtype: int
        """
        return self._image_width

    @image_width.setter
    def image_width(self, image_width):
        """Sets the image_width of this TiffOptions.

        Gets or sets the image width.

        :param image_width: The image_width of this TiffOptions.
        :type: int
        """
        if image_width is None:
            raise ValueError("Invalid value for `image_width`, must not be `None`")
        self._image_width = image_width

    @property
    def valid_tag_count(self):
        """Gets the valid_tag_count of this TiffOptions.

        Gets or sets the valid tag count.

        :return: The valid_tag_count of this TiffOptions.
        :rtype: int
        """
        return self._valid_tag_count

    @valid_tag_count.setter
    def valid_tag_count(self, valid_tag_count):
        """Sets the valid_tag_count of this TiffOptions.

        Gets or sets the valid tag count.

        :param valid_tag_count: The valid_tag_count of this TiffOptions.
        :type: int
        """
        if valid_tag_count is None:
            raise ValueError("Invalid value for `valid_tag_count`, must not be `None`")
        self._valid_tag_count = valid_tag_count

    @property
    def bits_per_pixel(self):
        """Gets the bits_per_pixel of this TiffOptions.

        Gets or sets the bits per pixel.

        :return: The bits_per_pixel of this TiffOptions.
        :rtype: int
        """
        return self._bits_per_pixel

    @bits_per_pixel.setter
    def bits_per_pixel(self, bits_per_pixel):
        """Sets the bits_per_pixel of this TiffOptions.

        Gets or sets the bits per pixel.

        :param bits_per_pixel: The bits_per_pixel of this TiffOptions.
        :type: int
        """
        if bits_per_pixel is None:
            raise ValueError("Invalid value for `bits_per_pixel`, must not be `None`")
        self._bits_per_pixel = bits_per_pixel

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TiffOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
