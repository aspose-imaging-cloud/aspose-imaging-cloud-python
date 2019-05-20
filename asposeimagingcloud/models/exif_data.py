# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="ExifData.py">
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
import pprint
import re  # noqa: F401

import six


class ExifData(object):
    """Represents common EXIF data section.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'aperture_value': 'float',
        'body_serial_number': 'str',
        'brightness_value': 'float',
        'cfa_pattern': 'str',
        'camera_owner_name': 'str',
        'color_space': 'str',
        'components_configuration': 'str',
        'compressed_bits_per_pixel': 'float',
        'contrast': 'str',
        'custom_rendered': 'str',
        'date_time_digitized': 'str',
        'date_time_original': 'str',
        'device_setting_description': 'str',
        'digital_zoom_ratio': 'float',
        'exif_version': 'str',
        'exposure_bias_value': 'float',
        'exposure_index': 'float',
        'exposure_mode': 'str',
        'exposure_program': 'str',
        'exposure_time': 'float',
        'f_number': 'float',
        'file_source': 'str',
        'flash': 'str',
        'flash_energy': 'float',
        'flashpix_version': 'str',
        'focal_length': 'float',
        'focal_length_in35_mm_film': 'int',
        'focal_plane_resolution_unit': 'str',
        'focal_plane_x_resolution': 'float',
        'focal_plane_y_resolution': 'float',
        'gps_altitude': 'float',
        'gps_altitude_ref': 'str',
        'gps_area_information': 'str',
        'gpsdop': 'float',
        'gps_dest_bearing': 'float',
        'gps_dest_bearing_ref': 'str',
        'gps_dest_distance': 'float',
        'gps_dest_distance_ref': 'str',
        'gps_dest_latitude': 'list[float]',
        'gps_dest_latitude_ref': 'str',
        'gps_dest_longitude': 'list[float]',
        'gps_dest_longitude_ref': 'str',
        'gps_differential': 'int',
        'gps_img_direction': 'float',
        'gps_img_direction_ref': 'str',
        'gps_date_stamp': 'str',
        'gps_latitude': 'list[float]',
        'gps_latitude_ref': 'str',
        'gps_longitude': 'list[float]',
        'gps_longitude_ref': 'str',
        'gps_map_datum': 'str',
        'gps_measure_mode': 'str',
        'gps_processing_method': 'str',
        'gps_satellites': 'str',
        'gps_speed': 'float',
        'gps_speed_ref': 'str',
        'gps_status': 'str',
        'gps_timestamp': 'list[float]',
        'gps_track': 'str',
        'gps_track_ref': 'str',
        'gps_version_id': 'str',
        'gain_control': 'str',
        'gamma': 'float',
        'iso_speed': 'int',
        'iso_speed_latitude_yyy': 'int',
        'iso_speed_latitude_zzz': 'int',
        'photographic_sensitivity': 'int',
        'image_unique_id': 'str',
        'lens_make': 'str',
        'lens_model': 'str',
        'lens_serial_number': 'str',
        'lens_specification': 'list[float]',
        'light_source': 'str',
        'maker_note_raw_data': 'str',
        'max_aperture_value': 'float',
        'metering_mode': 'str',
        'oecf': 'str',
        'pixel_x_dimension': 'int',
        'pixel_y_dimension': 'int',
        'recommended_exposure_index': 'int',
        'related_sound_file': 'str',
        'saturation': 'str',
        'scene_capture_type': 'str',
        'scene_type': 'int',
        'sensing_method': 'str',
        'sensitivity_type': 'int',
        'sharpness': 'int',
        'shutter_speed_value': 'float',
        'spatial_frequency_response': 'str',
        'spectral_sensitivity': 'str',
        'standard_output_sensitivity': 'int',
        'subject_area': 'list[int]',
        'subject_distance': 'float',
        'subject_distance_range': 'str',
        'subject_location': 'list[int]',
        'subsec_time': 'str',
        'subsec_time_digitized': 'str',
        'subsec_time_original': 'str',
        'user_comment': 'str',
        'white_balance': 'str',
        'white_point': 'list[float]'
    }

    attribute_map = {
        'aperture_value': 'ApertureValue',
        'body_serial_number': 'BodySerialNumber',
        'brightness_value': 'BrightnessValue',
        'cfa_pattern': 'CFAPattern',
        'camera_owner_name': 'CameraOwnerName',
        'color_space': 'ColorSpace',
        'components_configuration': 'ComponentsConfiguration',
        'compressed_bits_per_pixel': 'CompressedBitsPerPixel',
        'contrast': 'Contrast',
        'custom_rendered': 'CustomRendered',
        'date_time_digitized': 'DateTimeDigitized',
        'date_time_original': 'DateTimeOriginal',
        'device_setting_description': 'DeviceSettingDescription',
        'digital_zoom_ratio': 'DigitalZoomRatio',
        'exif_version': 'ExifVersion',
        'exposure_bias_value': 'ExposureBiasValue',
        'exposure_index': 'ExposureIndex',
        'exposure_mode': 'ExposureMode',
        'exposure_program': 'ExposureProgram',
        'exposure_time': 'ExposureTime',
        'f_number': 'FNumber',
        'file_source': 'FileSource',
        'flash': 'Flash',
        'flash_energy': 'FlashEnergy',
        'flashpix_version': 'FlashpixVersion',
        'focal_length': 'FocalLength',
        'focal_length_in35_mm_film': 'FocalLengthIn35MmFilm',
        'focal_plane_resolution_unit': 'FocalPlaneResolutionUnit',
        'focal_plane_x_resolution': 'FocalPlaneXResolution',
        'focal_plane_y_resolution': 'FocalPlaneYResolution',
        'gps_altitude': 'GPSAltitude',
        'gps_altitude_ref': 'GPSAltitudeRef',
        'gps_area_information': 'GPSAreaInformation',
        'gpsdop': 'GPSDOP',
        'gps_dest_bearing': 'GPSDestBearing',
        'gps_dest_bearing_ref': 'GPSDestBearingRef',
        'gps_dest_distance': 'GPSDestDistance',
        'gps_dest_distance_ref': 'GPSDestDistanceRef',
        'gps_dest_latitude': 'GPSDestLatitude',
        'gps_dest_latitude_ref': 'GPSDestLatitudeRef',
        'gps_dest_longitude': 'GPSDestLongitude',
        'gps_dest_longitude_ref': 'GPSDestLongitudeRef',
        'gps_differential': 'GPSDifferential',
        'gps_img_direction': 'GPSImgDirection',
        'gps_img_direction_ref': 'GPSImgDirectionRef',
        'gps_date_stamp': 'GPSDateStamp',
        'gps_latitude': 'GPSLatitude',
        'gps_latitude_ref': 'GPSLatitudeRef',
        'gps_longitude': 'GPSLongitude',
        'gps_longitude_ref': 'GPSLongitudeRef',
        'gps_map_datum': 'GPSMapDatum',
        'gps_measure_mode': 'GPSMeasureMode',
        'gps_processing_method': 'GPSProcessingMethod',
        'gps_satellites': 'GPSSatellites',
        'gps_speed': 'GPSSpeed',
        'gps_speed_ref': 'GPSSpeedRef',
        'gps_status': 'GPSStatus',
        'gps_timestamp': 'GPSTimestamp',
        'gps_track': 'GPSTrack',
        'gps_track_ref': 'GPSTrackRef',
        'gps_version_id': 'GPSVersionID',
        'gain_control': 'GainControl',
        'gamma': 'Gamma',
        'iso_speed': 'ISOSpeed',
        'iso_speed_latitude_yyy': 'ISOSpeedLatitudeYYY',
        'iso_speed_latitude_zzz': 'ISOSpeedLatitudeZZZ',
        'photographic_sensitivity': 'PhotographicSensitivity',
        'image_unique_id': 'ImageUniqueID',
        'lens_make': 'LensMake',
        'lens_model': 'LensModel',
        'lens_serial_number': 'LensSerialNumber',
        'lens_specification': 'LensSpecification',
        'light_source': 'LightSource',
        'maker_note_raw_data': 'MakerNoteRawData',
        'max_aperture_value': 'MaxApertureValue',
        'metering_mode': 'MeteringMode',
        'oecf': 'OECF',
        'pixel_x_dimension': 'PixelXDimension',
        'pixel_y_dimension': 'PixelYDimension',
        'recommended_exposure_index': 'RecommendedExposureIndex',
        'related_sound_file': 'RelatedSoundFile',
        'saturation': 'Saturation',
        'scene_capture_type': 'SceneCaptureType',
        'scene_type': 'SceneType',
        'sensing_method': 'SensingMethod',
        'sensitivity_type': 'SensitivityType',
        'sharpness': 'Sharpness',
        'shutter_speed_value': 'ShutterSpeedValue',
        'spatial_frequency_response': 'SpatialFrequencyResponse',
        'spectral_sensitivity': 'SpectralSensitivity',
        'standard_output_sensitivity': 'StandardOutputSensitivity',
        'subject_area': 'SubjectArea',
        'subject_distance': 'SubjectDistance',
        'subject_distance_range': 'SubjectDistanceRange',
        'subject_location': 'SubjectLocation',
        'subsec_time': 'SubsecTime',
        'subsec_time_digitized': 'SubsecTimeDigitized',
        'subsec_time_original': 'SubsecTimeOriginal',
        'user_comment': 'UserComment',
        'white_balance': 'WhiteBalance',
        'white_point': 'WhitePoint'
    }

    discriminator_value_class_map = {
        'JpegExifData': 'JpegExifData'
    }

    def __init__(self, aperture_value=None, body_serial_number=None, brightness_value=None, cfa_pattern=None, camera_owner_name=None, color_space=None, components_configuration=None, compressed_bits_per_pixel=None, contrast=None, custom_rendered=None, date_time_digitized=None, date_time_original=None, device_setting_description=None, digital_zoom_ratio=None, exif_version=None, exposure_bias_value=None, exposure_index=None, exposure_mode=None, exposure_program=None, exposure_time=None, f_number=None, file_source=None, flash=None, flash_energy=None, flashpix_version=None, focal_length=None, focal_length_in35_mm_film=None, focal_plane_resolution_unit=None, focal_plane_x_resolution=None, focal_plane_y_resolution=None, gps_altitude=None, gps_altitude_ref=None, gps_area_information=None, gpsdop=None, gps_dest_bearing=None, gps_dest_bearing_ref=None, gps_dest_distance=None, gps_dest_distance_ref=None, gps_dest_latitude=None, gps_dest_latitude_ref=None, gps_dest_longitude=None, gps_dest_longitude_ref=None, gps_differential=None, gps_img_direction=None, gps_img_direction_ref=None, gps_date_stamp=None, gps_latitude=None, gps_latitude_ref=None, gps_longitude=None, gps_longitude_ref=None, gps_map_datum=None, gps_measure_mode=None, gps_processing_method=None, gps_satellites=None, gps_speed=None, gps_speed_ref=None, gps_status=None, gps_timestamp=None, gps_track=None, gps_track_ref=None, gps_version_id=None, gain_control=None, gamma=None, iso_speed=None, iso_speed_latitude_yyy=None, iso_speed_latitude_zzz=None, photographic_sensitivity=None, image_unique_id=None, lens_make=None, lens_model=None, lens_serial_number=None, lens_specification=None, light_source=None, maker_note_raw_data=None, max_aperture_value=None, metering_mode=None, oecf=None, pixel_x_dimension=None, pixel_y_dimension=None, recommended_exposure_index=None, related_sound_file=None, saturation=None, scene_capture_type=None, scene_type=None, sensing_method=None, sensitivity_type=None, sharpness=None, shutter_speed_value=None, spatial_frequency_response=None, spectral_sensitivity=None, standard_output_sensitivity=None, subject_area=None, subject_distance=None, subject_distance_range=None, subject_location=None, subsec_time=None, subsec_time_digitized=None, subsec_time_original=None, user_comment=None, white_balance=None, white_point=None):  # noqa: E501
        """ExifData - a model defined in Swagger"""  # noqa: E501

        self._aperture_value = None
        self._body_serial_number = None
        self._brightness_value = None
        self._cfa_pattern = None
        self._camera_owner_name = None
        self._color_space = None
        self._components_configuration = None
        self._compressed_bits_per_pixel = None
        self._contrast = None
        self._custom_rendered = None
        self._date_time_digitized = None
        self._date_time_original = None
        self._device_setting_description = None
        self._digital_zoom_ratio = None
        self._exif_version = None
        self._exposure_bias_value = None
        self._exposure_index = None
        self._exposure_mode = None
        self._exposure_program = None
        self._exposure_time = None
        self._f_number = None
        self._file_source = None
        self._flash = None
        self._flash_energy = None
        self._flashpix_version = None
        self._focal_length = None
        self._focal_length_in35_mm_film = None
        self._focal_plane_resolution_unit = None
        self._focal_plane_x_resolution = None
        self._focal_plane_y_resolution = None
        self._gps_altitude = None
        self._gps_altitude_ref = None
        self._gps_area_information = None
        self._gpsdop = None
        self._gps_dest_bearing = None
        self._gps_dest_bearing_ref = None
        self._gps_dest_distance = None
        self._gps_dest_distance_ref = None
        self._gps_dest_latitude = None
        self._gps_dest_latitude_ref = None
        self._gps_dest_longitude = None
        self._gps_dest_longitude_ref = None
        self._gps_differential = None
        self._gps_img_direction = None
        self._gps_img_direction_ref = None
        self._gps_date_stamp = None
        self._gps_latitude = None
        self._gps_latitude_ref = None
        self._gps_longitude = None
        self._gps_longitude_ref = None
        self._gps_map_datum = None
        self._gps_measure_mode = None
        self._gps_processing_method = None
        self._gps_satellites = None
        self._gps_speed = None
        self._gps_speed_ref = None
        self._gps_status = None
        self._gps_timestamp = None
        self._gps_track = None
        self._gps_track_ref = None
        self._gps_version_id = None
        self._gain_control = None
        self._gamma = None
        self._iso_speed = None
        self._iso_speed_latitude_yyy = None
        self._iso_speed_latitude_zzz = None
        self._photographic_sensitivity = None
        self._image_unique_id = None
        self._lens_make = None
        self._lens_model = None
        self._lens_serial_number = None
        self._lens_specification = None
        self._light_source = None
        self._maker_note_raw_data = None
        self._max_aperture_value = None
        self._metering_mode = None
        self._oecf = None
        self._pixel_x_dimension = None
        self._pixel_y_dimension = None
        self._recommended_exposure_index = None
        self._related_sound_file = None
        self._saturation = None
        self._scene_capture_type = None
        self._scene_type = None
        self._sensing_method = None
        self._sensitivity_type = None
        self._sharpness = None
        self._shutter_speed_value = None
        self._spatial_frequency_response = None
        self._spectral_sensitivity = None
        self._standard_output_sensitivity = None
        self._subject_area = None
        self._subject_distance = None
        self._subject_distance_range = None
        self._subject_location = None
        self._subsec_time = None
        self._subsec_time_digitized = None
        self._subsec_time_original = None
        self._user_comment = None
        self._white_balance = None
        self._white_point = None
        self.discriminator = 'Type'

        if aperture_value is not None:
            self.aperture_value = aperture_value
        if body_serial_number is not None:
            self.body_serial_number = body_serial_number
        if brightness_value is not None:
            self.brightness_value = brightness_value
        if cfa_pattern is not None:
            self.cfa_pattern = cfa_pattern
        if camera_owner_name is not None:
            self.camera_owner_name = camera_owner_name
        if color_space is not None:
            self.color_space = color_space
        if components_configuration is not None:
            self.components_configuration = components_configuration
        if compressed_bits_per_pixel is not None:
            self.compressed_bits_per_pixel = compressed_bits_per_pixel
        if contrast is not None:
            self.contrast = contrast
        if custom_rendered is not None:
            self.custom_rendered = custom_rendered
        if date_time_digitized is not None:
            self.date_time_digitized = date_time_digitized
        if date_time_original is not None:
            self.date_time_original = date_time_original
        if device_setting_description is not None:
            self.device_setting_description = device_setting_description
        if digital_zoom_ratio is not None:
            self.digital_zoom_ratio = digital_zoom_ratio
        if exif_version is not None:
            self.exif_version = exif_version
        if exposure_bias_value is not None:
            self.exposure_bias_value = exposure_bias_value
        if exposure_index is not None:
            self.exposure_index = exposure_index
        if exposure_mode is not None:
            self.exposure_mode = exposure_mode
        if exposure_program is not None:
            self.exposure_program = exposure_program
        if exposure_time is not None:
            self.exposure_time = exposure_time
        if f_number is not None:
            self.f_number = f_number
        if file_source is not None:
            self.file_source = file_source
        if flash is not None:
            self.flash = flash
        if flash_energy is not None:
            self.flash_energy = flash_energy
        if flashpix_version is not None:
            self.flashpix_version = flashpix_version
        if focal_length is not None:
            self.focal_length = focal_length
        if focal_length_in35_mm_film is not None:
            self.focal_length_in35_mm_film = focal_length_in35_mm_film
        if focal_plane_resolution_unit is not None:
            self.focal_plane_resolution_unit = focal_plane_resolution_unit
        if focal_plane_x_resolution is not None:
            self.focal_plane_x_resolution = focal_plane_x_resolution
        if focal_plane_y_resolution is not None:
            self.focal_plane_y_resolution = focal_plane_y_resolution
        if gps_altitude is not None:
            self.gps_altitude = gps_altitude
        if gps_altitude_ref is not None:
            self.gps_altitude_ref = gps_altitude_ref
        if gps_area_information is not None:
            self.gps_area_information = gps_area_information
        if gpsdop is not None:
            self.gpsdop = gpsdop
        if gps_dest_bearing is not None:
            self.gps_dest_bearing = gps_dest_bearing
        if gps_dest_bearing_ref is not None:
            self.gps_dest_bearing_ref = gps_dest_bearing_ref
        if gps_dest_distance is not None:
            self.gps_dest_distance = gps_dest_distance
        if gps_dest_distance_ref is not None:
            self.gps_dest_distance_ref = gps_dest_distance_ref
        if gps_dest_latitude is not None:
            self.gps_dest_latitude = gps_dest_latitude
        if gps_dest_latitude_ref is not None:
            self.gps_dest_latitude_ref = gps_dest_latitude_ref
        if gps_dest_longitude is not None:
            self.gps_dest_longitude = gps_dest_longitude
        if gps_dest_longitude_ref is not None:
            self.gps_dest_longitude_ref = gps_dest_longitude_ref
        if gps_differential is not None:
            self.gps_differential = gps_differential
        if gps_img_direction is not None:
            self.gps_img_direction = gps_img_direction
        if gps_img_direction_ref is not None:
            self.gps_img_direction_ref = gps_img_direction_ref
        if gps_date_stamp is not None:
            self.gps_date_stamp = gps_date_stamp
        if gps_latitude is not None:
            self.gps_latitude = gps_latitude
        if gps_latitude_ref is not None:
            self.gps_latitude_ref = gps_latitude_ref
        if gps_longitude is not None:
            self.gps_longitude = gps_longitude
        if gps_longitude_ref is not None:
            self.gps_longitude_ref = gps_longitude_ref
        if gps_map_datum is not None:
            self.gps_map_datum = gps_map_datum
        if gps_measure_mode is not None:
            self.gps_measure_mode = gps_measure_mode
        if gps_processing_method is not None:
            self.gps_processing_method = gps_processing_method
        if gps_satellites is not None:
            self.gps_satellites = gps_satellites
        if gps_speed is not None:
            self.gps_speed = gps_speed
        if gps_speed_ref is not None:
            self.gps_speed_ref = gps_speed_ref
        if gps_status is not None:
            self.gps_status = gps_status
        if gps_timestamp is not None:
            self.gps_timestamp = gps_timestamp
        if gps_track is not None:
            self.gps_track = gps_track
        if gps_track_ref is not None:
            self.gps_track_ref = gps_track_ref
        if gps_version_id is not None:
            self.gps_version_id = gps_version_id
        if gain_control is not None:
            self.gain_control = gain_control
        if gamma is not None:
            self.gamma = gamma
        if iso_speed is not None:
            self.iso_speed = iso_speed
        if iso_speed_latitude_yyy is not None:
            self.iso_speed_latitude_yyy = iso_speed_latitude_yyy
        if iso_speed_latitude_zzz is not None:
            self.iso_speed_latitude_zzz = iso_speed_latitude_zzz
        if photographic_sensitivity is not None:
            self.photographic_sensitivity = photographic_sensitivity
        if image_unique_id is not None:
            self.image_unique_id = image_unique_id
        if lens_make is not None:
            self.lens_make = lens_make
        if lens_model is not None:
            self.lens_model = lens_model
        if lens_serial_number is not None:
            self.lens_serial_number = lens_serial_number
        if lens_specification is not None:
            self.lens_specification = lens_specification
        if light_source is not None:
            self.light_source = light_source
        if maker_note_raw_data is not None:
            self.maker_note_raw_data = maker_note_raw_data
        if max_aperture_value is not None:
            self.max_aperture_value = max_aperture_value
        if metering_mode is not None:
            self.metering_mode = metering_mode
        if oecf is not None:
            self.oecf = oecf
        if pixel_x_dimension is not None:
            self.pixel_x_dimension = pixel_x_dimension
        if pixel_y_dimension is not None:
            self.pixel_y_dimension = pixel_y_dimension
        if recommended_exposure_index is not None:
            self.recommended_exposure_index = recommended_exposure_index
        if related_sound_file is not None:
            self.related_sound_file = related_sound_file
        if saturation is not None:
            self.saturation = saturation
        if scene_capture_type is not None:
            self.scene_capture_type = scene_capture_type
        if scene_type is not None:
            self.scene_type = scene_type
        if sensing_method is not None:
            self.sensing_method = sensing_method
        if sensitivity_type is not None:
            self.sensitivity_type = sensitivity_type
        if sharpness is not None:
            self.sharpness = sharpness
        if shutter_speed_value is not None:
            self.shutter_speed_value = shutter_speed_value
        if spatial_frequency_response is not None:
            self.spatial_frequency_response = spatial_frequency_response
        if spectral_sensitivity is not None:
            self.spectral_sensitivity = spectral_sensitivity
        if standard_output_sensitivity is not None:
            self.standard_output_sensitivity = standard_output_sensitivity
        if subject_area is not None:
            self.subject_area = subject_area
        if subject_distance is not None:
            self.subject_distance = subject_distance
        if subject_distance_range is not None:
            self.subject_distance_range = subject_distance_range
        if subject_location is not None:
            self.subject_location = subject_location
        if subsec_time is not None:
            self.subsec_time = subsec_time
        if subsec_time_digitized is not None:
            self.subsec_time_digitized = subsec_time_digitized
        if subsec_time_original is not None:
            self.subsec_time_original = subsec_time_original
        if user_comment is not None:
            self.user_comment = user_comment
        if white_balance is not None:
            self.white_balance = white_balance
        if white_point is not None:
            self.white_point = white_point

    @property
    def aperture_value(self):
        """Gets the aperture_value of this ExifData.  # noqa: E501

        Gets or sets the aperture.  # noqa: E501

        :return: The aperture_value of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._aperture_value

    @aperture_value.setter
    def aperture_value(self, aperture_value):
        """Sets the aperture_value of this ExifData.

        Gets or sets the aperture.  # noqa: E501

        :param aperture_value: The aperture_value of this ExifData.  # noqa: E501
        :type: float
        """
        if aperture_value is None:
            raise ValueError("Invalid value for `aperture_value`, must not be `None`")  # noqa: E501
        self._aperture_value = aperture_value

    @property
    def body_serial_number(self):
        """Gets the body_serial_number of this ExifData.  # noqa: E501

        Gets or sets the body serial number.  # noqa: E501

        :return: The body_serial_number of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._body_serial_number

    @body_serial_number.setter
    def body_serial_number(self, body_serial_number):
        """Sets the body_serial_number of this ExifData.

        Gets or sets the body serial number.  # noqa: E501

        :param body_serial_number: The body_serial_number of this ExifData.  # noqa: E501
        :type: str
        """
        self._body_serial_number = body_serial_number

    @property
    def brightness_value(self):
        """Gets the brightness_value of this ExifData.  # noqa: E501

        Gets or sets the brightness.  # noqa: E501

        :return: The brightness_value of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._brightness_value

    @brightness_value.setter
    def brightness_value(self, brightness_value):
        """Sets the brightness_value of this ExifData.

        Gets or sets the brightness.  # noqa: E501

        :param brightness_value: The brightness_value of this ExifData.  # noqa: E501
        :type: float
        """
        if brightness_value is None:
            raise ValueError("Invalid value for `brightness_value`, must not be `None`")  # noqa: E501
        self._brightness_value = brightness_value

    @property
    def cfa_pattern(self):
        """Gets the cfa_pattern of this ExifData.  # noqa: E501

        Gets or sets the CFA pattern.  # noqa: E501

        :return: The cfa_pattern of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._cfa_pattern

    @cfa_pattern.setter
    def cfa_pattern(self, cfa_pattern):
        """Sets the cfa_pattern of this ExifData.

        Gets or sets the CFA pattern.  # noqa: E501

        :param cfa_pattern: The cfa_pattern of this ExifData.  # noqa: E501
        :type: str
        """
        if cfa_pattern is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', cfa_pattern):  # noqa: E501
            raise ValueError("Invalid value for `cfa_pattern`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501
        self._cfa_pattern = cfa_pattern

    @property
    def camera_owner_name(self):
        """Gets the camera_owner_name of this ExifData.  # noqa: E501

        Gets or sets the camera owner name.  # noqa: E501

        :return: The camera_owner_name of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._camera_owner_name

    @camera_owner_name.setter
    def camera_owner_name(self, camera_owner_name):
        """Sets the camera_owner_name of this ExifData.

        Gets or sets the camera owner name.  # noqa: E501

        :param camera_owner_name: The camera_owner_name of this ExifData.  # noqa: E501
        :type: str
        """
        self._camera_owner_name = camera_owner_name

    @property
    def color_space(self):
        """Gets the color_space of this ExifData.  # noqa: E501

        Gets or sets the color space.  # noqa: E501

        :return: The color_space of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._color_space

    @color_space.setter
    def color_space(self, color_space):
        """Sets the color_space of this ExifData.

        Gets or sets the color space.  # noqa: E501

        :param color_space: The color_space of this ExifData.  # noqa: E501
        :type: str
        """
        self._color_space = color_space

    @property
    def components_configuration(self):
        """Gets the components_configuration of this ExifData.  # noqa: E501

        Gets or sets the components configuration.  # noqa: E501

        :return: The components_configuration of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._components_configuration

    @components_configuration.setter
    def components_configuration(self, components_configuration):
        """Sets the components_configuration of this ExifData.

        Gets or sets the components configuration.  # noqa: E501

        :param components_configuration: The components_configuration of this ExifData.  # noqa: E501
        :type: str
        """
        if components_configuration is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', components_configuration):  # noqa: E501
            raise ValueError("Invalid value for `components_configuration`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501
        self._components_configuration = components_configuration

    @property
    def compressed_bits_per_pixel(self):
        """Gets the compressed_bits_per_pixel of this ExifData.  # noqa: E501

        Gets or sets the compressed bits per pixel.  # noqa: E501

        :return: The compressed_bits_per_pixel of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._compressed_bits_per_pixel

    @compressed_bits_per_pixel.setter
    def compressed_bits_per_pixel(self, compressed_bits_per_pixel):
        """Sets the compressed_bits_per_pixel of this ExifData.

        Gets or sets the compressed bits per pixel.  # noqa: E501

        :param compressed_bits_per_pixel: The compressed_bits_per_pixel of this ExifData.  # noqa: E501
        :type: float
        """
        if compressed_bits_per_pixel is None:
            raise ValueError("Invalid value for `compressed_bits_per_pixel`, must not be `None`")  # noqa: E501
        self._compressed_bits_per_pixel = compressed_bits_per_pixel

    @property
    def contrast(self):
        """Gets the contrast of this ExifData.  # noqa: E501

        Gets or sets the contrast.  # noqa: E501

        :return: The contrast of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._contrast

    @contrast.setter
    def contrast(self, contrast):
        """Sets the contrast of this ExifData.

        Gets or sets the contrast.  # noqa: E501

        :param contrast: The contrast of this ExifData.  # noqa: E501
        :type: str
        """
        self._contrast = contrast

    @property
    def custom_rendered(self):
        """Gets the custom_rendered of this ExifData.  # noqa: E501

        Gets or sets the value indincating if custom rendering is performed.  # noqa: E501

        :return: The custom_rendered of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._custom_rendered

    @custom_rendered.setter
    def custom_rendered(self, custom_rendered):
        """Sets the custom_rendered of this ExifData.

        Gets or sets the value indincating if custom rendering is performed.  # noqa: E501

        :param custom_rendered: The custom_rendered of this ExifData.  # noqa: E501
        :type: str
        """
        self._custom_rendered = custom_rendered

    @property
    def date_time_digitized(self):
        """Gets the date_time_digitized of this ExifData.  # noqa: E501

        Gets or sets date and time when image was digitized.  # noqa: E501

        :return: The date_time_digitized of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._date_time_digitized

    @date_time_digitized.setter
    def date_time_digitized(self, date_time_digitized):
        """Sets the date_time_digitized of this ExifData.

        Gets or sets date and time when image was digitized.  # noqa: E501

        :param date_time_digitized: The date_time_digitized of this ExifData.  # noqa: E501
        :type: str
        """
        self._date_time_digitized = date_time_digitized

    @property
    def date_time_original(self):
        """Gets the date_time_original of this ExifData.  # noqa: E501

        Gets or sets date and time of the original image.  # noqa: E501

        :return: The date_time_original of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._date_time_original

    @date_time_original.setter
    def date_time_original(self, date_time_original):
        """Sets the date_time_original of this ExifData.

        Gets or sets date and time of the original image.  # noqa: E501

        :param date_time_original: The date_time_original of this ExifData.  # noqa: E501
        :type: str
        """
        self._date_time_original = date_time_original

    @property
    def device_setting_description(self):
        """Gets the device_setting_description of this ExifData.  # noqa: E501

        Gets or sets the device setting description.  # noqa: E501

        :return: The device_setting_description of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._device_setting_description

    @device_setting_description.setter
    def device_setting_description(self, device_setting_description):
        """Sets the device_setting_description of this ExifData.

        Gets or sets the device setting description.  # noqa: E501

        :param device_setting_description: The device_setting_description of this ExifData.  # noqa: E501
        :type: str
        """
        if device_setting_description is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', device_setting_description):  # noqa: E501
            raise ValueError("Invalid value for `device_setting_description`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501
        self._device_setting_description = device_setting_description

    @property
    def digital_zoom_ratio(self):
        """Gets the digital_zoom_ratio of this ExifData.  # noqa: E501

        Gets or sets the digital zoom ratio.  # noqa: E501

        :return: The digital_zoom_ratio of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._digital_zoom_ratio

    @digital_zoom_ratio.setter
    def digital_zoom_ratio(self, digital_zoom_ratio):
        """Sets the digital_zoom_ratio of this ExifData.

        Gets or sets the digital zoom ratio.  # noqa: E501

        :param digital_zoom_ratio: The digital_zoom_ratio of this ExifData.  # noqa: E501
        :type: float
        """
        if digital_zoom_ratio is None:
            raise ValueError("Invalid value for `digital_zoom_ratio`, must not be `None`")  # noqa: E501
        self._digital_zoom_ratio = digital_zoom_ratio

    @property
    def exif_version(self):
        """Gets the exif_version of this ExifData.  # noqa: E501

        Gets or sets EXIF version.  # noqa: E501

        :return: The exif_version of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._exif_version

    @exif_version.setter
    def exif_version(self, exif_version):
        """Sets the exif_version of this ExifData.

        Gets or sets EXIF version.  # noqa: E501

        :param exif_version: The exif_version of this ExifData.  # noqa: E501
        :type: str
        """
        if exif_version is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', exif_version):  # noqa: E501
            raise ValueError("Invalid value for `exif_version`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501
        self._exif_version = exif_version

    @property
    def exposure_bias_value(self):
        """Gets the exposure_bias_value of this ExifData.  # noqa: E501

        Gets or sets the exposure bias.  # noqa: E501

        :return: The exposure_bias_value of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._exposure_bias_value

    @exposure_bias_value.setter
    def exposure_bias_value(self, exposure_bias_value):
        """Sets the exposure_bias_value of this ExifData.

        Gets or sets the exposure bias.  # noqa: E501

        :param exposure_bias_value: The exposure_bias_value of this ExifData.  # noqa: E501
        :type: float
        """
        if exposure_bias_value is None:
            raise ValueError("Invalid value for `exposure_bias_value`, must not be `None`")  # noqa: E501
        self._exposure_bias_value = exposure_bias_value

    @property
    def exposure_index(self):
        """Gets the exposure_index of this ExifData.  # noqa: E501

        Gets or sets the exposure index.  # noqa: E501

        :return: The exposure_index of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._exposure_index

    @exposure_index.setter
    def exposure_index(self, exposure_index):
        """Sets the exposure_index of this ExifData.

        Gets or sets the exposure index.  # noqa: E501

        :param exposure_index: The exposure_index of this ExifData.  # noqa: E501
        :type: float
        """
        if exposure_index is None:
            raise ValueError("Invalid value for `exposure_index`, must not be `None`")  # noqa: E501
        self._exposure_index = exposure_index

    @property
    def exposure_mode(self):
        """Gets the exposure_mode of this ExifData.  # noqa: E501

        Gets or sets the exposure mode.  # noqa: E501

        :return: The exposure_mode of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._exposure_mode

    @exposure_mode.setter
    def exposure_mode(self, exposure_mode):
        """Sets the exposure_mode of this ExifData.

        Gets or sets the exposure mode.  # noqa: E501

        :param exposure_mode: The exposure_mode of this ExifData.  # noqa: E501
        :type: str
        """
        self._exposure_mode = exposure_mode

    @property
    def exposure_program(self):
        """Gets the exposure_program of this ExifData.  # noqa: E501

        Gets or sets the exposure program.  # noqa: E501

        :return: The exposure_program of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._exposure_program

    @exposure_program.setter
    def exposure_program(self, exposure_program):
        """Sets the exposure_program of this ExifData.

        Gets or sets the exposure program.  # noqa: E501

        :param exposure_program: The exposure_program of this ExifData.  # noqa: E501
        :type: str
        """
        self._exposure_program = exposure_program

    @property
    def exposure_time(self):
        """Gets the exposure_time of this ExifData.  # noqa: E501

        Gets or sets the exposure time.  # noqa: E501

        :return: The exposure_time of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._exposure_time

    @exposure_time.setter
    def exposure_time(self, exposure_time):
        """Sets the exposure_time of this ExifData.

        Gets or sets the exposure time.  # noqa: E501

        :param exposure_time: The exposure_time of this ExifData.  # noqa: E501
        :type: float
        """
        if exposure_time is None:
            raise ValueError("Invalid value for `exposure_time`, must not be `None`")  # noqa: E501
        self._exposure_time = exposure_time

    @property
    def f_number(self):
        """Gets the f_number of this ExifData.  # noqa: E501

        Gets or sets the focal number.  # noqa: E501

        :return: The f_number of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._f_number

    @f_number.setter
    def f_number(self, f_number):
        """Sets the f_number of this ExifData.

        Gets or sets the focal number.  # noqa: E501

        :param f_number: The f_number of this ExifData.  # noqa: E501
        :type: float
        """
        if f_number is None:
            raise ValueError("Invalid value for `f_number`, must not be `None`")  # noqa: E501
        self._f_number = f_number

    @property
    def file_source(self):
        """Gets the file_source of this ExifData.  # noqa: E501

        Gets or sets the file source.  # noqa: E501

        :return: The file_source of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._file_source

    @file_source.setter
    def file_source(self, file_source):
        """Sets the file_source of this ExifData.

        Gets or sets the file source.  # noqa: E501

        :param file_source: The file_source of this ExifData.  # noqa: E501
        :type: str
        """
        self._file_source = file_source

    @property
    def flash(self):
        """Gets the flash of this ExifData.  # noqa: E501

        Gets or sets the flash.  # noqa: E501

        :return: The flash of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._flash

    @flash.setter
    def flash(self, flash):
        """Sets the flash of this ExifData.

        Gets or sets the flash.  # noqa: E501

        :param flash: The flash of this ExifData.  # noqa: E501
        :type: str
        """
        self._flash = flash

    @property
    def flash_energy(self):
        """Gets the flash_energy of this ExifData.  # noqa: E501

        Gets or sets the flash energy.  # noqa: E501

        :return: The flash_energy of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._flash_energy

    @flash_energy.setter
    def flash_energy(self, flash_energy):
        """Sets the flash_energy of this ExifData.

        Gets or sets the flash energy.  # noqa: E501

        :param flash_energy: The flash_energy of this ExifData.  # noqa: E501
        :type: float
        """
        if flash_energy is None:
            raise ValueError("Invalid value for `flash_energy`, must not be `None`")  # noqa: E501
        self._flash_energy = flash_energy

    @property
    def flashpix_version(self):
        """Gets the flashpix_version of this ExifData.  # noqa: E501

        Gets or sets the Flashpix version.  # noqa: E501

        :return: The flashpix_version of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._flashpix_version

    @flashpix_version.setter
    def flashpix_version(self, flashpix_version):
        """Sets the flashpix_version of this ExifData.

        Gets or sets the Flashpix version.  # noqa: E501

        :param flashpix_version: The flashpix_version of this ExifData.  # noqa: E501
        :type: str
        """
        if flashpix_version is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', flashpix_version):  # noqa: E501
            raise ValueError("Invalid value for `flashpix_version`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501
        self._flashpix_version = flashpix_version

    @property
    def focal_length(self):
        """Gets the focal_length of this ExifData.  # noqa: E501

        Gets or sets the focal length.  # noqa: E501

        :return: The focal_length of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._focal_length

    @focal_length.setter
    def focal_length(self, focal_length):
        """Sets the focal_length of this ExifData.

        Gets or sets the focal length.  # noqa: E501

        :param focal_length: The focal_length of this ExifData.  # noqa: E501
        :type: float
        """
        if focal_length is None:
            raise ValueError("Invalid value for `focal_length`, must not be `None`")  # noqa: E501
        self._focal_length = focal_length

    @property
    def focal_length_in35_mm_film(self):
        """Gets the focal_length_in35_mm_film of this ExifData.  # noqa: E501

        Gets or sets the focal length in 35mm film.  # noqa: E501

        :return: The focal_length_in35_mm_film of this ExifData.  # noqa: E501
        :rtype: int
        """
        return self._focal_length_in35_mm_film

    @focal_length_in35_mm_film.setter
    def focal_length_in35_mm_film(self, focal_length_in35_mm_film):
        """Sets the focal_length_in35_mm_film of this ExifData.

        Gets or sets the focal length in 35mm film.  # noqa: E501

        :param focal_length_in35_mm_film: The focal_length_in35_mm_film of this ExifData.  # noqa: E501
        :type: int
        """
        if focal_length_in35_mm_film is None:
            raise ValueError("Invalid value for `focal_length_in35_mm_film`, must not be `None`")  # noqa: E501
        self._focal_length_in35_mm_film = focal_length_in35_mm_film

    @property
    def focal_plane_resolution_unit(self):
        """Gets the focal_plane_resolution_unit of this ExifData.  # noqa: E501

        Gets or sets the focal plane resolution unit.  # noqa: E501

        :return: The focal_plane_resolution_unit of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._focal_plane_resolution_unit

    @focal_plane_resolution_unit.setter
    def focal_plane_resolution_unit(self, focal_plane_resolution_unit):
        """Sets the focal_plane_resolution_unit of this ExifData.

        Gets or sets the focal plane resolution unit.  # noqa: E501

        :param focal_plane_resolution_unit: The focal_plane_resolution_unit of this ExifData.  # noqa: E501
        :type: str
        """
        self._focal_plane_resolution_unit = focal_plane_resolution_unit

    @property
    def focal_plane_x_resolution(self):
        """Gets the focal_plane_x_resolution of this ExifData.  # noqa: E501

        Gets or sets the focal plane X resolution.  # noqa: E501

        :return: The focal_plane_x_resolution of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._focal_plane_x_resolution

    @focal_plane_x_resolution.setter
    def focal_plane_x_resolution(self, focal_plane_x_resolution):
        """Sets the focal_plane_x_resolution of this ExifData.

        Gets or sets the focal plane X resolution.  # noqa: E501

        :param focal_plane_x_resolution: The focal_plane_x_resolution of this ExifData.  # noqa: E501
        :type: float
        """
        if focal_plane_x_resolution is None:
            raise ValueError("Invalid value for `focal_plane_x_resolution`, must not be `None`")  # noqa: E501
        self._focal_plane_x_resolution = focal_plane_x_resolution

    @property
    def focal_plane_y_resolution(self):
        """Gets the focal_plane_y_resolution of this ExifData.  # noqa: E501

        Gets or sets the focal plane Y resolution.  # noqa: E501

        :return: The focal_plane_y_resolution of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._focal_plane_y_resolution

    @focal_plane_y_resolution.setter
    def focal_plane_y_resolution(self, focal_plane_y_resolution):
        """Sets the focal_plane_y_resolution of this ExifData.

        Gets or sets the focal plane Y resolution.  # noqa: E501

        :param focal_plane_y_resolution: The focal_plane_y_resolution of this ExifData.  # noqa: E501
        :type: float
        """
        if focal_plane_y_resolution is None:
            raise ValueError("Invalid value for `focal_plane_y_resolution`, must not be `None`")  # noqa: E501
        self._focal_plane_y_resolution = focal_plane_y_resolution

    @property
    def gps_altitude(self):
        """Gets the gps_altitude of this ExifData.  # noqa: E501

        Gets or sets the GPS altitude.  # noqa: E501

        :return: The gps_altitude of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._gps_altitude

    @gps_altitude.setter
    def gps_altitude(self, gps_altitude):
        """Sets the gps_altitude of this ExifData.

        Gets or sets the GPS altitude.  # noqa: E501

        :param gps_altitude: The gps_altitude of this ExifData.  # noqa: E501
        :type: float
        """
        if gps_altitude is None:
            raise ValueError("Invalid value for `gps_altitude`, must not be `None`")  # noqa: E501
        self._gps_altitude = gps_altitude

    @property
    def gps_altitude_ref(self):
        """Gets the gps_altitude_ref of this ExifData.  # noqa: E501

        Gets or sets the GPS altitude reference (if it's above or below sea level).  # noqa: E501

        :return: The gps_altitude_ref of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._gps_altitude_ref

    @gps_altitude_ref.setter
    def gps_altitude_ref(self, gps_altitude_ref):
        """Sets the gps_altitude_ref of this ExifData.

        Gets or sets the GPS altitude reference (if it's above or below sea level).  # noqa: E501

        :param gps_altitude_ref: The gps_altitude_ref of this ExifData.  # noqa: E501
        :type: str
        """
        self._gps_altitude_ref = gps_altitude_ref

    @property
    def gps_area_information(self):
        """Gets the gps_area_information of this ExifData.  # noqa: E501

        Gets or sets the GPS area information.  # noqa: E501

        :return: The gps_area_information of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._gps_area_information

    @gps_area_information.setter
    def gps_area_information(self, gps_area_information):
        """Sets the gps_area_information of this ExifData.

        Gets or sets the GPS area information.  # noqa: E501

        :param gps_area_information: The gps_area_information of this ExifData.  # noqa: E501
        :type: str
        """
        if gps_area_information is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', gps_area_information):  # noqa: E501
            raise ValueError("Invalid value for `gps_area_information`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501
        self._gps_area_information = gps_area_information

    @property
    def gpsdop(self):
        """Gets the gpsdop of this ExifData.  # noqa: E501

        Gets or sets the GPS DOP (data degree of precision).  # noqa: E501

        :return: The gpsdop of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._gpsdop

    @gpsdop.setter
    def gpsdop(self, gpsdop):
        """Sets the gpsdop of this ExifData.

        Gets or sets the GPS DOP (data degree of precision).  # noqa: E501

        :param gpsdop: The gpsdop of this ExifData.  # noqa: E501
        :type: float
        """
        if gpsdop is None:
            raise ValueError("Invalid value for `gpsdop`, must not be `None`")  # noqa: E501
        self._gpsdop = gpsdop

    @property
    def gps_dest_bearing(self):
        """Gets the gps_dest_bearing of this ExifData.  # noqa: E501

        Gets or sets the GPS bearing of the destination.  # noqa: E501

        :return: The gps_dest_bearing of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._gps_dest_bearing

    @gps_dest_bearing.setter
    def gps_dest_bearing(self, gps_dest_bearing):
        """Sets the gps_dest_bearing of this ExifData.

        Gets or sets the GPS bearing of the destination.  # noqa: E501

        :param gps_dest_bearing: The gps_dest_bearing of this ExifData.  # noqa: E501
        :type: float
        """
        if gps_dest_bearing is None:
            raise ValueError("Invalid value for `gps_dest_bearing`, must not be `None`")  # noqa: E501
        self._gps_dest_bearing = gps_dest_bearing

    @property
    def gps_dest_bearing_ref(self):
        """Gets the gps_dest_bearing_ref of this ExifData.  # noqa: E501

        Gets or sets the GPS reference unit for bearing of the destination.  # noqa: E501

        :return: The gps_dest_bearing_ref of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._gps_dest_bearing_ref

    @gps_dest_bearing_ref.setter
    def gps_dest_bearing_ref(self, gps_dest_bearing_ref):
        """Sets the gps_dest_bearing_ref of this ExifData.

        Gets or sets the GPS reference unit for bearing of the destination.  # noqa: E501

        :param gps_dest_bearing_ref: The gps_dest_bearing_ref of this ExifData.  # noqa: E501
        :type: str
        """
        self._gps_dest_bearing_ref = gps_dest_bearing_ref

    @property
    def gps_dest_distance(self):
        """Gets the gps_dest_distance of this ExifData.  # noqa: E501

        Gets or sets the GPS destination distance.  # noqa: E501

        :return: The gps_dest_distance of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._gps_dest_distance

    @gps_dest_distance.setter
    def gps_dest_distance(self, gps_dest_distance):
        """Sets the gps_dest_distance of this ExifData.

        Gets or sets the GPS destination distance.  # noqa: E501

        :param gps_dest_distance: The gps_dest_distance of this ExifData.  # noqa: E501
        :type: float
        """
        if gps_dest_distance is None:
            raise ValueError("Invalid value for `gps_dest_distance`, must not be `None`")  # noqa: E501
        self._gps_dest_distance = gps_dest_distance

    @property
    def gps_dest_distance_ref(self):
        """Gets the gps_dest_distance_ref of this ExifData.  # noqa: E501

        Gets or sets the GPS reference unit for destination distance.  # noqa: E501

        :return: The gps_dest_distance_ref of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._gps_dest_distance_ref

    @gps_dest_distance_ref.setter
    def gps_dest_distance_ref(self, gps_dest_distance_ref):
        """Sets the gps_dest_distance_ref of this ExifData.

        Gets or sets the GPS reference unit for destination distance.  # noqa: E501

        :param gps_dest_distance_ref: The gps_dest_distance_ref of this ExifData.  # noqa: E501
        :type: str
        """
        self._gps_dest_distance_ref = gps_dest_distance_ref

    @property
    def gps_dest_latitude(self):
        """Gets the gps_dest_latitude of this ExifData.  # noqa: E501

        Gets or sets the GPS destination latitude.  # noqa: E501

        :return: The gps_dest_latitude of this ExifData.  # noqa: E501
        :rtype: list[float]
        """
        return self._gps_dest_latitude

    @gps_dest_latitude.setter
    def gps_dest_latitude(self, gps_dest_latitude):
        """Sets the gps_dest_latitude of this ExifData.

        Gets or sets the GPS destination latitude.  # noqa: E501

        :param gps_dest_latitude: The gps_dest_latitude of this ExifData.  # noqa: E501
        :type: list[float]
        """
        self._gps_dest_latitude = gps_dest_latitude

    @property
    def gps_dest_latitude_ref(self):
        """Gets the gps_dest_latitude_ref of this ExifData.  # noqa: E501

        Gets or sets the GPS reference destination latitude (north or south).  # noqa: E501

        :return: The gps_dest_latitude_ref of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._gps_dest_latitude_ref

    @gps_dest_latitude_ref.setter
    def gps_dest_latitude_ref(self, gps_dest_latitude_ref):
        """Sets the gps_dest_latitude_ref of this ExifData.

        Gets or sets the GPS reference destination latitude (north or south).  # noqa: E501

        :param gps_dest_latitude_ref: The gps_dest_latitude_ref of this ExifData.  # noqa: E501
        :type: str
        """
        self._gps_dest_latitude_ref = gps_dest_latitude_ref

    @property
    def gps_dest_longitude(self):
        """Gets the gps_dest_longitude of this ExifData.  # noqa: E501

        Gets or sets the GPS destination longtitude.  # noqa: E501

        :return: The gps_dest_longitude of this ExifData.  # noqa: E501
        :rtype: list[float]
        """
        return self._gps_dest_longitude

    @gps_dest_longitude.setter
    def gps_dest_longitude(self, gps_dest_longitude):
        """Sets the gps_dest_longitude of this ExifData.

        Gets or sets the GPS destination longtitude.  # noqa: E501

        :param gps_dest_longitude: The gps_dest_longitude of this ExifData.  # noqa: E501
        :type: list[float]
        """
        self._gps_dest_longitude = gps_dest_longitude

    @property
    def gps_dest_longitude_ref(self):
        """Gets the gps_dest_longitude_ref of this ExifData.  # noqa: E501

        Gets or sets the GPS reference destination longtitude (east or west).  # noqa: E501

        :return: The gps_dest_longitude_ref of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._gps_dest_longitude_ref

    @gps_dest_longitude_ref.setter
    def gps_dest_longitude_ref(self, gps_dest_longitude_ref):
        """Sets the gps_dest_longitude_ref of this ExifData.

        Gets or sets the GPS reference destination longtitude (east or west).  # noqa: E501

        :param gps_dest_longitude_ref: The gps_dest_longitude_ref of this ExifData.  # noqa: E501
        :type: str
        """
        self._gps_dest_longitude_ref = gps_dest_longitude_ref

    @property
    def gps_differential(self):
        """Gets the gps_differential of this ExifData.  # noqa: E501

        Gets or sets the GPS differential.  # noqa: E501

        :return: The gps_differential of this ExifData.  # noqa: E501
        :rtype: int
        """
        return self._gps_differential

    @gps_differential.setter
    def gps_differential(self, gps_differential):
        """Sets the gps_differential of this ExifData.

        Gets or sets the GPS differential.  # noqa: E501

        :param gps_differential: The gps_differential of this ExifData.  # noqa: E501
        :type: int
        """
        if gps_differential is None:
            raise ValueError("Invalid value for `gps_differential`, must not be `None`")  # noqa: E501
        self._gps_differential = gps_differential

    @property
    def gps_img_direction(self):
        """Gets the gps_img_direction of this ExifData.  # noqa: E501

        Gets or sets the GPS image direction.  # noqa: E501

        :return: The gps_img_direction of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._gps_img_direction

    @gps_img_direction.setter
    def gps_img_direction(self, gps_img_direction):
        """Sets the gps_img_direction of this ExifData.

        Gets or sets the GPS image direction.  # noqa: E501

        :param gps_img_direction: The gps_img_direction of this ExifData.  # noqa: E501
        :type: float
        """
        if gps_img_direction is None:
            raise ValueError("Invalid value for `gps_img_direction`, must not be `None`")  # noqa: E501
        self._gps_img_direction = gps_img_direction

    @property
    def gps_img_direction_ref(self):
        """Gets the gps_img_direction_ref of this ExifData.  # noqa: E501

        Gets or sets the GPS reference image direction.  # noqa: E501

        :return: The gps_img_direction_ref of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._gps_img_direction_ref

    @gps_img_direction_ref.setter
    def gps_img_direction_ref(self, gps_img_direction_ref):
        """Sets the gps_img_direction_ref of this ExifData.

        Gets or sets the GPS reference image direction.  # noqa: E501

        :param gps_img_direction_ref: The gps_img_direction_ref of this ExifData.  # noqa: E501
        :type: str
        """
        self._gps_img_direction_ref = gps_img_direction_ref

    @property
    def gps_date_stamp(self):
        """Gets the gps_date_stamp of this ExifData.  # noqa: E501

        Gets or sets the GPS date stamp.  # noqa: E501

        :return: The gps_date_stamp of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._gps_date_stamp

    @gps_date_stamp.setter
    def gps_date_stamp(self, gps_date_stamp):
        """Sets the gps_date_stamp of this ExifData.

        Gets or sets the GPS date stamp.  # noqa: E501

        :param gps_date_stamp: The gps_date_stamp of this ExifData.  # noqa: E501
        :type: str
        """
        self._gps_date_stamp = gps_date_stamp

    @property
    def gps_latitude(self):
        """Gets the gps_latitude of this ExifData.  # noqa: E501

        Gets or sets the GPS latitude.  # noqa: E501

        :return: The gps_latitude of this ExifData.  # noqa: E501
        :rtype: list[float]
        """
        return self._gps_latitude

    @gps_latitude.setter
    def gps_latitude(self, gps_latitude):
        """Sets the gps_latitude of this ExifData.

        Gets or sets the GPS latitude.  # noqa: E501

        :param gps_latitude: The gps_latitude of this ExifData.  # noqa: E501
        :type: list[float]
        """
        self._gps_latitude = gps_latitude

    @property
    def gps_latitude_ref(self):
        """Gets the gps_latitude_ref of this ExifData.  # noqa: E501

        Gets or sets the GPS latitude reference (north or south).  # noqa: E501

        :return: The gps_latitude_ref of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._gps_latitude_ref

    @gps_latitude_ref.setter
    def gps_latitude_ref(self, gps_latitude_ref):
        """Sets the gps_latitude_ref of this ExifData.

        Gets or sets the GPS latitude reference (north or south).  # noqa: E501

        :param gps_latitude_ref: The gps_latitude_ref of this ExifData.  # noqa: E501
        :type: str
        """
        self._gps_latitude_ref = gps_latitude_ref

    @property
    def gps_longitude(self):
        """Gets the gps_longitude of this ExifData.  # noqa: E501

        Gets or sets the GPS longitude.  # noqa: E501

        :return: The gps_longitude of this ExifData.  # noqa: E501
        :rtype: list[float]
        """
        return self._gps_longitude

    @gps_longitude.setter
    def gps_longitude(self, gps_longitude):
        """Sets the gps_longitude of this ExifData.

        Gets or sets the GPS longitude.  # noqa: E501

        :param gps_longitude: The gps_longitude of this ExifData.  # noqa: E501
        :type: list[float]
        """
        self._gps_longitude = gps_longitude

    @property
    def gps_longitude_ref(self):
        """Gets the gps_longitude_ref of this ExifData.  # noqa: E501

        Gets or sets the GPS longitude reference (east or west).  # noqa: E501

        :return: The gps_longitude_ref of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._gps_longitude_ref

    @gps_longitude_ref.setter
    def gps_longitude_ref(self, gps_longitude_ref):
        """Sets the gps_longitude_ref of this ExifData.

        Gets or sets the GPS longitude reference (east or west).  # noqa: E501

        :param gps_longitude_ref: The gps_longitude_ref of this ExifData.  # noqa: E501
        :type: str
        """
        self._gps_longitude_ref = gps_longitude_ref

    @property
    def gps_map_datum(self):
        """Gets the gps_map_datum of this ExifData.  # noqa: E501

        Gets or sets the geodetic survey data used by the GPS receiver.  # noqa: E501

        :return: The gps_map_datum of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._gps_map_datum

    @gps_map_datum.setter
    def gps_map_datum(self, gps_map_datum):
        """Sets the gps_map_datum of this ExifData.

        Gets or sets the geodetic survey data used by the GPS receiver.  # noqa: E501

        :param gps_map_datum: The gps_map_datum of this ExifData.  # noqa: E501
        :type: str
        """
        self._gps_map_datum = gps_map_datum

    @property
    def gps_measure_mode(self):
        """Gets the gps_measure_mode of this ExifData.  # noqa: E501

        Gets or sets the GPS measure mode.  # noqa: E501

        :return: The gps_measure_mode of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._gps_measure_mode

    @gps_measure_mode.setter
    def gps_measure_mode(self, gps_measure_mode):
        """Sets the gps_measure_mode of this ExifData.

        Gets or sets the GPS measure mode.  # noqa: E501

        :param gps_measure_mode: The gps_measure_mode of this ExifData.  # noqa: E501
        :type: str
        """
        self._gps_measure_mode = gps_measure_mode

    @property
    def gps_processing_method(self):
        """Gets the gps_processing_method of this ExifData.  # noqa: E501

        Gets or setsthe GPS processing method.  # noqa: E501

        :return: The gps_processing_method of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._gps_processing_method

    @gps_processing_method.setter
    def gps_processing_method(self, gps_processing_method):
        """Sets the gps_processing_method of this ExifData.

        Gets or setsthe GPS processing method.  # noqa: E501

        :param gps_processing_method: The gps_processing_method of this ExifData.  # noqa: E501
        :type: str
        """
        if gps_processing_method is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', gps_processing_method):  # noqa: E501
            raise ValueError("Invalid value for `gps_processing_method`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501
        self._gps_processing_method = gps_processing_method

    @property
    def gps_satellites(self):
        """Gets the gps_satellites of this ExifData.  # noqa: E501

        Gets or sets the GPS satellites info.  # noqa: E501

        :return: The gps_satellites of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._gps_satellites

    @gps_satellites.setter
    def gps_satellites(self, gps_satellites):
        """Sets the gps_satellites of this ExifData.

        Gets or sets the GPS satellites info.  # noqa: E501

        :param gps_satellites: The gps_satellites of this ExifData.  # noqa: E501
        :type: str
        """
        self._gps_satellites = gps_satellites

    @property
    def gps_speed(self):
        """Gets the gps_speed of this ExifData.  # noqa: E501

        Gets or sets the GPS speed.  # noqa: E501

        :return: The gps_speed of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._gps_speed

    @gps_speed.setter
    def gps_speed(self, gps_speed):
        """Sets the gps_speed of this ExifData.

        Gets or sets the GPS speed.  # noqa: E501

        :param gps_speed: The gps_speed of this ExifData.  # noqa: E501
        :type: float
        """
        if gps_speed is None:
            raise ValueError("Invalid value for `gps_speed`, must not be `None`")  # noqa: E501
        self._gps_speed = gps_speed

    @property
    def gps_speed_ref(self):
        """Gets the gps_speed_ref of this ExifData.  # noqa: E501

        Gets or sets the GPS speed reference unit.  # noqa: E501

        :return: The gps_speed_ref of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._gps_speed_ref

    @gps_speed_ref.setter
    def gps_speed_ref(self, gps_speed_ref):
        """Sets the gps_speed_ref of this ExifData.

        Gets or sets the GPS speed reference unit.  # noqa: E501

        :param gps_speed_ref: The gps_speed_ref of this ExifData.  # noqa: E501
        :type: str
        """
        self._gps_speed_ref = gps_speed_ref

    @property
    def gps_status(self):
        """Gets the gps_status of this ExifData.  # noqa: E501

        Gets or sets the GPS status.  # noqa: E501

        :return: The gps_status of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._gps_status

    @gps_status.setter
    def gps_status(self, gps_status):
        """Sets the gps_status of this ExifData.

        Gets or sets the GPS status.  # noqa: E501

        :param gps_status: The gps_status of this ExifData.  # noqa: E501
        :type: str
        """
        self._gps_status = gps_status

    @property
    def gps_timestamp(self):
        """Gets the gps_timestamp of this ExifData.  # noqa: E501

        Gets or sets the GPS times tamp.  # noqa: E501

        :return: The gps_timestamp of this ExifData.  # noqa: E501
        :rtype: list[float]
        """
        return self._gps_timestamp

    @gps_timestamp.setter
    def gps_timestamp(self, gps_timestamp):
        """Sets the gps_timestamp of this ExifData.

        Gets or sets the GPS times tamp.  # noqa: E501

        :param gps_timestamp: The gps_timestamp of this ExifData.  # noqa: E501
        :type: list[float]
        """
        self._gps_timestamp = gps_timestamp

    @property
    def gps_track(self):
        """Gets the gps_track of this ExifData.  # noqa: E501

        Gets or sets the GPS track.  # noqa: E501

        :return: The gps_track of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._gps_track

    @gps_track.setter
    def gps_track(self, gps_track):
        """Sets the gps_track of this ExifData.

        Gets or sets the GPS track.  # noqa: E501

        :param gps_track: The gps_track of this ExifData.  # noqa: E501
        :type: str
        """
        self._gps_track = gps_track

    @property
    def gps_track_ref(self):
        """Gets the gps_track_ref of this ExifData.  # noqa: E501

        Gets or sets the GPS track reference.  # noqa: E501

        :return: The gps_track_ref of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._gps_track_ref

    @gps_track_ref.setter
    def gps_track_ref(self, gps_track_ref):
        """Sets the gps_track_ref of this ExifData.

        Gets or sets the GPS track reference.  # noqa: E501

        :param gps_track_ref: The gps_track_ref of this ExifData.  # noqa: E501
        :type: str
        """
        self._gps_track_ref = gps_track_ref

    @property
    def gps_version_id(self):
        """Gets the gps_version_id of this ExifData.  # noqa: E501

        Gets or sets the GPS version ID.  # noqa: E501

        :return: The gps_version_id of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._gps_version_id

    @gps_version_id.setter
    def gps_version_id(self, gps_version_id):
        """Sets the gps_version_id of this ExifData.

        Gets or sets the GPS version ID.  # noqa: E501

        :param gps_version_id: The gps_version_id of this ExifData.  # noqa: E501
        :type: str
        """
        if gps_version_id is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', gps_version_id):  # noqa: E501
            raise ValueError("Invalid value for `gps_version_id`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501
        self._gps_version_id = gps_version_id

    @property
    def gain_control(self):
        """Gets the gain_control of this ExifData.  # noqa: E501

        Gets or sets the gain control.  # noqa: E501

        :return: The gain_control of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._gain_control

    @gain_control.setter
    def gain_control(self, gain_control):
        """Sets the gain_control of this ExifData.

        Gets or sets the gain control.  # noqa: E501

        :param gain_control: The gain_control of this ExifData.  # noqa: E501
        :type: str
        """
        self._gain_control = gain_control

    @property
    def gamma(self):
        """Gets the gamma of this ExifData.  # noqa: E501

        Gets or sets the gamma.  # noqa: E501

        :return: The gamma of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._gamma

    @gamma.setter
    def gamma(self, gamma):
        """Sets the gamma of this ExifData.

        Gets or sets the gamma.  # noqa: E501

        :param gamma: The gamma of this ExifData.  # noqa: E501
        :type: float
        """
        if gamma is None:
            raise ValueError("Invalid value for `gamma`, must not be `None`")  # noqa: E501
        self._gamma = gamma

    @property
    def iso_speed(self):
        """Gets the iso_speed of this ExifData.  # noqa: E501

        Gets or sets the ISO speed.  # noqa: E501

        :return: The iso_speed of this ExifData.  # noqa: E501
        :rtype: int
        """
        return self._iso_speed

    @iso_speed.setter
    def iso_speed(self, iso_speed):
        """Sets the iso_speed of this ExifData.

        Gets or sets the ISO speed.  # noqa: E501

        :param iso_speed: The iso_speed of this ExifData.  # noqa: E501
        :type: int
        """
        if iso_speed is None:
            raise ValueError("Invalid value for `iso_speed`, must not be `None`")  # noqa: E501
        self._iso_speed = iso_speed

    @property
    def iso_speed_latitude_yyy(self):
        """Gets the iso_speed_latitude_yyy of this ExifData.  # noqa: E501

        Gets or sets the ISO speed latitude YYY value.  # noqa: E501

        :return: The iso_speed_latitude_yyy of this ExifData.  # noqa: E501
        :rtype: int
        """
        return self._iso_speed_latitude_yyy

    @iso_speed_latitude_yyy.setter
    def iso_speed_latitude_yyy(self, iso_speed_latitude_yyy):
        """Sets the iso_speed_latitude_yyy of this ExifData.

        Gets or sets the ISO speed latitude YYY value.  # noqa: E501

        :param iso_speed_latitude_yyy: The iso_speed_latitude_yyy of this ExifData.  # noqa: E501
        :type: int
        """
        if iso_speed_latitude_yyy is None:
            raise ValueError("Invalid value for `iso_speed_latitude_yyy`, must not be `None`")  # noqa: E501
        self._iso_speed_latitude_yyy = iso_speed_latitude_yyy

    @property
    def iso_speed_latitude_zzz(self):
        """Gets the iso_speed_latitude_zzz of this ExifData.  # noqa: E501

        Gets or sets the ISO speed latitude ZZZ value.  # noqa: E501

        :return: The iso_speed_latitude_zzz of this ExifData.  # noqa: E501
        :rtype: int
        """
        return self._iso_speed_latitude_zzz

    @iso_speed_latitude_zzz.setter
    def iso_speed_latitude_zzz(self, iso_speed_latitude_zzz):
        """Sets the iso_speed_latitude_zzz of this ExifData.

        Gets or sets the ISO speed latitude ZZZ value.  # noqa: E501

        :param iso_speed_latitude_zzz: The iso_speed_latitude_zzz of this ExifData.  # noqa: E501
        :type: int
        """
        if iso_speed_latitude_zzz is None:
            raise ValueError("Invalid value for `iso_speed_latitude_zzz`, must not be `None`")  # noqa: E501
        self._iso_speed_latitude_zzz = iso_speed_latitude_zzz

    @property
    def photographic_sensitivity(self):
        """Gets the photographic_sensitivity of this ExifData.  # noqa: E501

        Gets or sets the photographic sensitivity.  # noqa: E501

        :return: The photographic_sensitivity of this ExifData.  # noqa: E501
        :rtype: int
        """
        return self._photographic_sensitivity

    @photographic_sensitivity.setter
    def photographic_sensitivity(self, photographic_sensitivity):
        """Sets the photographic_sensitivity of this ExifData.

        Gets or sets the photographic sensitivity.  # noqa: E501

        :param photographic_sensitivity: The photographic_sensitivity of this ExifData.  # noqa: E501
        :type: int
        """
        if photographic_sensitivity is None:
            raise ValueError("Invalid value for `photographic_sensitivity`, must not be `None`")  # noqa: E501
        self._photographic_sensitivity = photographic_sensitivity

    @property
    def image_unique_id(self):
        """Gets the image_unique_id of this ExifData.  # noqa: E501

        Gets or sets the image unique ID.  # noqa: E501

        :return: The image_unique_id of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._image_unique_id

    @image_unique_id.setter
    def image_unique_id(self, image_unique_id):
        """Sets the image_unique_id of this ExifData.

        Gets or sets the image unique ID.  # noqa: E501

        :param image_unique_id: The image_unique_id of this ExifData.  # noqa: E501
        :type: str
        """
        self._image_unique_id = image_unique_id

    @property
    def lens_make(self):
        """Gets the lens_make of this ExifData.  # noqa: E501

        Gets or sets the lens manufacturer.  # noqa: E501

        :return: The lens_make of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._lens_make

    @lens_make.setter
    def lens_make(self, lens_make):
        """Sets the lens_make of this ExifData.

        Gets or sets the lens manufacturer.  # noqa: E501

        :param lens_make: The lens_make of this ExifData.  # noqa: E501
        :type: str
        """
        self._lens_make = lens_make

    @property
    def lens_model(self):
        """Gets the lens_model of this ExifData.  # noqa: E501

        Gets or sets the lens model.  # noqa: E501

        :return: The lens_model of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._lens_model

    @lens_model.setter
    def lens_model(self, lens_model):
        """Sets the lens_model of this ExifData.

        Gets or sets the lens model.  # noqa: E501

        :param lens_model: The lens_model of this ExifData.  # noqa: E501
        :type: str
        """
        self._lens_model = lens_model

    @property
    def lens_serial_number(self):
        """Gets the lens_serial_number of this ExifData.  # noqa: E501

        Gets or sets the lens serial number.  # noqa: E501

        :return: The lens_serial_number of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._lens_serial_number

    @lens_serial_number.setter
    def lens_serial_number(self, lens_serial_number):
        """Sets the lens_serial_number of this ExifData.

        Gets or sets the lens serial number.  # noqa: E501

        :param lens_serial_number: The lens_serial_number of this ExifData.  # noqa: E501
        :type: str
        """
        self._lens_serial_number = lens_serial_number

    @property
    def lens_specification(self):
        """Gets the lens_specification of this ExifData.  # noqa: E501

        Gets or sets the lens specification.  # noqa: E501

        :return: The lens_specification of this ExifData.  # noqa: E501
        :rtype: list[float]
        """
        return self._lens_specification

    @lens_specification.setter
    def lens_specification(self, lens_specification):
        """Sets the lens_specification of this ExifData.

        Gets or sets the lens specification.  # noqa: E501

        :param lens_specification: The lens_specification of this ExifData.  # noqa: E501
        :type: list[float]
        """
        self._lens_specification = lens_specification

    @property
    def light_source(self):
        """Gets the light_source of this ExifData.  # noqa: E501

        Gets or sets the light source.  # noqa: E501

        :return: The light_source of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._light_source

    @light_source.setter
    def light_source(self, light_source):
        """Sets the light_source of this ExifData.

        Gets or sets the light source.  # noqa: E501

        :param light_source: The light_source of this ExifData.  # noqa: E501
        :type: str
        """
        self._light_source = light_source

    @property
    def maker_note_raw_data(self):
        """Gets the maker_note_raw_data of this ExifData.  # noqa: E501

        Gets or sets the maker note raw data.  # noqa: E501

        :return: The maker_note_raw_data of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._maker_note_raw_data

    @maker_note_raw_data.setter
    def maker_note_raw_data(self, maker_note_raw_data):
        """Sets the maker_note_raw_data of this ExifData.

        Gets or sets the maker note raw data.  # noqa: E501

        :param maker_note_raw_data: The maker_note_raw_data of this ExifData.  # noqa: E501
        :type: str
        """
        if maker_note_raw_data is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', maker_note_raw_data):  # noqa: E501
            raise ValueError("Invalid value for `maker_note_raw_data`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501
        self._maker_note_raw_data = maker_note_raw_data

    @property
    def max_aperture_value(self):
        """Gets the max_aperture_value of this ExifData.  # noqa: E501

        Gets or sets the max aperture.  # noqa: E501

        :return: The max_aperture_value of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._max_aperture_value

    @max_aperture_value.setter
    def max_aperture_value(self, max_aperture_value):
        """Sets the max_aperture_value of this ExifData.

        Gets or sets the max aperture.  # noqa: E501

        :param max_aperture_value: The max_aperture_value of this ExifData.  # noqa: E501
        :type: float
        """
        if max_aperture_value is None:
            raise ValueError("Invalid value for `max_aperture_value`, must not be `None`")  # noqa: E501
        self._max_aperture_value = max_aperture_value

    @property
    def metering_mode(self):
        """Gets the metering_mode of this ExifData.  # noqa: E501

        Gets or sets the metering mode.  # noqa: E501

        :return: The metering_mode of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._metering_mode

    @metering_mode.setter
    def metering_mode(self, metering_mode):
        """Sets the metering_mode of this ExifData.

        Gets or sets the metering mode.  # noqa: E501

        :param metering_mode: The metering_mode of this ExifData.  # noqa: E501
        :type: str
        """
        self._metering_mode = metering_mode

    @property
    def oecf(self):
        """Gets the oecf of this ExifData.  # noqa: E501

        Gets or sets the OECF (Opto-Electric Conversion Function).  # noqa: E501

        :return: The oecf of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._oecf

    @oecf.setter
    def oecf(self, oecf):
        """Sets the oecf of this ExifData.

        Gets or sets the OECF (Opto-Electric Conversion Function).  # noqa: E501

        :param oecf: The oecf of this ExifData.  # noqa: E501
        :type: str
        """
        if oecf is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', oecf):  # noqa: E501
            raise ValueError("Invalid value for `oecf`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501
        self._oecf = oecf

    @property
    def pixel_x_dimension(self):
        """Gets the pixel_x_dimension of this ExifData.  # noqa: E501

        Gets or sets the pixel X dimension.  # noqa: E501

        :return: The pixel_x_dimension of this ExifData.  # noqa: E501
        :rtype: int
        """
        return self._pixel_x_dimension

    @pixel_x_dimension.setter
    def pixel_x_dimension(self, pixel_x_dimension):
        """Sets the pixel_x_dimension of this ExifData.

        Gets or sets the pixel X dimension.  # noqa: E501

        :param pixel_x_dimension: The pixel_x_dimension of this ExifData.  # noqa: E501
        :type: int
        """
        if pixel_x_dimension is None:
            raise ValueError("Invalid value for `pixel_x_dimension`, must not be `None`")  # noqa: E501
        self._pixel_x_dimension = pixel_x_dimension

    @property
    def pixel_y_dimension(self):
        """Gets the pixel_y_dimension of this ExifData.  # noqa: E501

        Gets or sets the pixel Y dimension.  # noqa: E501

        :return: The pixel_y_dimension of this ExifData.  # noqa: E501
        :rtype: int
        """
        return self._pixel_y_dimension

    @pixel_y_dimension.setter
    def pixel_y_dimension(self, pixel_y_dimension):
        """Sets the pixel_y_dimension of this ExifData.

        Gets or sets the pixel Y dimension.  # noqa: E501

        :param pixel_y_dimension: The pixel_y_dimension of this ExifData.  # noqa: E501
        :type: int
        """
        if pixel_y_dimension is None:
            raise ValueError("Invalid value for `pixel_y_dimension`, must not be `None`")  # noqa: E501
        self._pixel_y_dimension = pixel_y_dimension

    @property
    def recommended_exposure_index(self):
        """Gets the recommended_exposure_index of this ExifData.  # noqa: E501

        Gets or sets the recommended exposure index.  # noqa: E501

        :return: The recommended_exposure_index of this ExifData.  # noqa: E501
        :rtype: int
        """
        return self._recommended_exposure_index

    @recommended_exposure_index.setter
    def recommended_exposure_index(self, recommended_exposure_index):
        """Sets the recommended_exposure_index of this ExifData.

        Gets or sets the recommended exposure index.  # noqa: E501

        :param recommended_exposure_index: The recommended_exposure_index of this ExifData.  # noqa: E501
        :type: int
        """
        if recommended_exposure_index is None:
            raise ValueError("Invalid value for `recommended_exposure_index`, must not be `None`")  # noqa: E501
        self._recommended_exposure_index = recommended_exposure_index

    @property
    def related_sound_file(self):
        """Gets the related_sound_file of this ExifData.  # noqa: E501

        Gets or sets the related sound file.  # noqa: E501

        :return: The related_sound_file of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._related_sound_file

    @related_sound_file.setter
    def related_sound_file(self, related_sound_file):
        """Sets the related_sound_file of this ExifData.

        Gets or sets the related sound file.  # noqa: E501

        :param related_sound_file: The related_sound_file of this ExifData.  # noqa: E501
        :type: str
        """
        self._related_sound_file = related_sound_file

    @property
    def saturation(self):
        """Gets the saturation of this ExifData.  # noqa: E501

        Gets or sets the saturation.  # noqa: E501

        :return: The saturation of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._saturation

    @saturation.setter
    def saturation(self, saturation):
        """Sets the saturation of this ExifData.

        Gets or sets the saturation.  # noqa: E501

        :param saturation: The saturation of this ExifData.  # noqa: E501
        :type: str
        """
        self._saturation = saturation

    @property
    def scene_capture_type(self):
        """Gets the scene_capture_type of this ExifData.  # noqa: E501

        Gets or sets the scene capture type.  # noqa: E501

        :return: The scene_capture_type of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._scene_capture_type

    @scene_capture_type.setter
    def scene_capture_type(self, scene_capture_type):
        """Sets the scene_capture_type of this ExifData.

        Gets or sets the scene capture type.  # noqa: E501

        :param scene_capture_type: The scene_capture_type of this ExifData.  # noqa: E501
        :type: str
        """
        self._scene_capture_type = scene_capture_type

    @property
    def scene_type(self):
        """Gets the scene_type of this ExifData.  # noqa: E501

        Gets or sets the scene type.  # noqa: E501

        :return: The scene_type of this ExifData.  # noqa: E501
        :rtype: int
        """
        return self._scene_type

    @scene_type.setter
    def scene_type(self, scene_type):
        """Sets the scene_type of this ExifData.

        Gets or sets the scene type.  # noqa: E501

        :param scene_type: The scene_type of this ExifData.  # noqa: E501
        :type: int
        """
        if scene_type is None:
            raise ValueError("Invalid value for `scene_type`, must not be `None`")  # noqa: E501
        self._scene_type = scene_type

    @property
    def sensing_method(self):
        """Gets the sensing_method of this ExifData.  # noqa: E501

        Gets or sets the sensing method.  # noqa: E501

        :return: The sensing_method of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._sensing_method

    @sensing_method.setter
    def sensing_method(self, sensing_method):
        """Sets the sensing_method of this ExifData.

        Gets or sets the sensing method.  # noqa: E501

        :param sensing_method: The sensing_method of this ExifData.  # noqa: E501
        :type: str
        """
        self._sensing_method = sensing_method

    @property
    def sensitivity_type(self):
        """Gets the sensitivity_type of this ExifData.  # noqa: E501

        Gets or sets the sensitivity type.  # noqa: E501

        :return: The sensitivity_type of this ExifData.  # noqa: E501
        :rtype: int
        """
        return self._sensitivity_type

    @sensitivity_type.setter
    def sensitivity_type(self, sensitivity_type):
        """Sets the sensitivity_type of this ExifData.

        Gets or sets the sensitivity type.  # noqa: E501

        :param sensitivity_type: The sensitivity_type of this ExifData.  # noqa: E501
        :type: int
        """
        if sensitivity_type is None:
            raise ValueError("Invalid value for `sensitivity_type`, must not be `None`")  # noqa: E501
        self._sensitivity_type = sensitivity_type

    @property
    def sharpness(self):
        """Gets the sharpness of this ExifData.  # noqa: E501

        Gets or sets the sharpness.  # noqa: E501

        :return: The sharpness of this ExifData.  # noqa: E501
        :rtype: int
        """
        return self._sharpness

    @sharpness.setter
    def sharpness(self, sharpness):
        """Sets the sharpness of this ExifData.

        Gets or sets the sharpness.  # noqa: E501

        :param sharpness: The sharpness of this ExifData.  # noqa: E501
        :type: int
        """
        if sharpness is None:
            raise ValueError("Invalid value for `sharpness`, must not be `None`")  # noqa: E501
        self._sharpness = sharpness

    @property
    def shutter_speed_value(self):
        """Gets the shutter_speed_value of this ExifData.  # noqa: E501

        Gets or sets the shutter speed.  # noqa: E501

        :return: The shutter_speed_value of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._shutter_speed_value

    @shutter_speed_value.setter
    def shutter_speed_value(self, shutter_speed_value):
        """Sets the shutter_speed_value of this ExifData.

        Gets or sets the shutter speed.  # noqa: E501

        :param shutter_speed_value: The shutter_speed_value of this ExifData.  # noqa: E501
        :type: float
        """
        if shutter_speed_value is None:
            raise ValueError("Invalid value for `shutter_speed_value`, must not be `None`")  # noqa: E501
        self._shutter_speed_value = shutter_speed_value

    @property
    def spatial_frequency_response(self):
        """Gets the spatial_frequency_response of this ExifData.  # noqa: E501

        Gets or sets the spatial frequency response.  # noqa: E501

        :return: The spatial_frequency_response of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._spatial_frequency_response

    @spatial_frequency_response.setter
    def spatial_frequency_response(self, spatial_frequency_response):
        """Sets the spatial_frequency_response of this ExifData.

        Gets or sets the spatial frequency response.  # noqa: E501

        :param spatial_frequency_response: The spatial_frequency_response of this ExifData.  # noqa: E501
        :type: str
        """
        if spatial_frequency_response is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', spatial_frequency_response):  # noqa: E501
            raise ValueError("Invalid value for `spatial_frequency_response`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501
        self._spatial_frequency_response = spatial_frequency_response

    @property
    def spectral_sensitivity(self):
        """Gets the spectral_sensitivity of this ExifData.  # noqa: E501

        Gets or sets the spectral sensitivity.  # noqa: E501

        :return: The spectral_sensitivity of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._spectral_sensitivity

    @spectral_sensitivity.setter
    def spectral_sensitivity(self, spectral_sensitivity):
        """Sets the spectral_sensitivity of this ExifData.

        Gets or sets the spectral sensitivity.  # noqa: E501

        :param spectral_sensitivity: The spectral_sensitivity of this ExifData.  # noqa: E501
        :type: str
        """
        self._spectral_sensitivity = spectral_sensitivity

    @property
    def standard_output_sensitivity(self):
        """Gets the standard_output_sensitivity of this ExifData.  # noqa: E501

        Gets or sets the standard output sensitivity.  # noqa: E501

        :return: The standard_output_sensitivity of this ExifData.  # noqa: E501
        :rtype: int
        """
        return self._standard_output_sensitivity

    @standard_output_sensitivity.setter
    def standard_output_sensitivity(self, standard_output_sensitivity):
        """Sets the standard_output_sensitivity of this ExifData.

        Gets or sets the standard output sensitivity.  # noqa: E501

        :param standard_output_sensitivity: The standard_output_sensitivity of this ExifData.  # noqa: E501
        :type: int
        """
        if standard_output_sensitivity is None:
            raise ValueError("Invalid value for `standard_output_sensitivity`, must not be `None`")  # noqa: E501
        self._standard_output_sensitivity = standard_output_sensitivity

    @property
    def subject_area(self):
        """Gets the subject_area of this ExifData.  # noqa: E501

        Gets or sets the subject area.  # noqa: E501

        :return: The subject_area of this ExifData.  # noqa: E501
        :rtype: list[int]
        """
        return self._subject_area

    @subject_area.setter
    def subject_area(self, subject_area):
        """Sets the subject_area of this ExifData.

        Gets or sets the subject area.  # noqa: E501

        :param subject_area: The subject_area of this ExifData.  # noqa: E501
        :type: list[int]
        """
        self._subject_area = subject_area

    @property
    def subject_distance(self):
        """Gets the subject_distance of this ExifData.  # noqa: E501

        Gets or sets the subject distance.  # noqa: E501

        :return: The subject_distance of this ExifData.  # noqa: E501
        :rtype: float
        """
        return self._subject_distance

    @subject_distance.setter
    def subject_distance(self, subject_distance):
        """Sets the subject_distance of this ExifData.

        Gets or sets the subject distance.  # noqa: E501

        :param subject_distance: The subject_distance of this ExifData.  # noqa: E501
        :type: float
        """
        if subject_distance is None:
            raise ValueError("Invalid value for `subject_distance`, must not be `None`")  # noqa: E501
        self._subject_distance = subject_distance

    @property
    def subject_distance_range(self):
        """Gets the subject_distance_range of this ExifData.  # noqa: E501

        Gets or sets the subject distance range.  # noqa: E501

        :return: The subject_distance_range of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._subject_distance_range

    @subject_distance_range.setter
    def subject_distance_range(self, subject_distance_range):
        """Sets the subject_distance_range of this ExifData.

        Gets or sets the subject distance range.  # noqa: E501

        :param subject_distance_range: The subject_distance_range of this ExifData.  # noqa: E501
        :type: str
        """
        self._subject_distance_range = subject_distance_range

    @property
    def subject_location(self):
        """Gets the subject_location of this ExifData.  # noqa: E501

        Gets or sets the subject location.  # noqa: E501

        :return: The subject_location of this ExifData.  # noqa: E501
        :rtype: list[int]
        """
        return self._subject_location

    @subject_location.setter
    def subject_location(self, subject_location):
        """Sets the subject_location of this ExifData.

        Gets or sets the subject location.  # noqa: E501

        :param subject_location: The subject_location of this ExifData.  # noqa: E501
        :type: list[int]
        """
        self._subject_location = subject_location

    @property
    def subsec_time(self):
        """Gets the subsec_time of this ExifData.  # noqa: E501

        Gets or sets the fractions of seconds for the DateTime tag.  # noqa: E501

        :return: The subsec_time of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._subsec_time

    @subsec_time.setter
    def subsec_time(self, subsec_time):
        """Sets the subsec_time of this ExifData.

        Gets or sets the fractions of seconds for the DateTime tag.  # noqa: E501

        :param subsec_time: The subsec_time of this ExifData.  # noqa: E501
        :type: str
        """
        self._subsec_time = subsec_time

    @property
    def subsec_time_digitized(self):
        """Gets the subsec_time_digitized of this ExifData.  # noqa: E501

        Gets or sets the fractions of seconds for the DateTimeDigitized tag.  # noqa: E501

        :return: The subsec_time_digitized of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._subsec_time_digitized

    @subsec_time_digitized.setter
    def subsec_time_digitized(self, subsec_time_digitized):
        """Sets the subsec_time_digitized of this ExifData.

        Gets or sets the fractions of seconds for the DateTimeDigitized tag.  # noqa: E501

        :param subsec_time_digitized: The subsec_time_digitized of this ExifData.  # noqa: E501
        :type: str
        """
        self._subsec_time_digitized = subsec_time_digitized

    @property
    def subsec_time_original(self):
        """Gets the subsec_time_original of this ExifData.  # noqa: E501

        Gets or sets the fractions of seconds for the DateTimeOriginal tag.  # noqa: E501

        :return: The subsec_time_original of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._subsec_time_original

    @subsec_time_original.setter
    def subsec_time_original(self, subsec_time_original):
        """Sets the subsec_time_original of this ExifData.

        Gets or sets the fractions of seconds for the DateTimeOriginal tag.  # noqa: E501

        :param subsec_time_original: The subsec_time_original of this ExifData.  # noqa: E501
        :type: str
        """
        self._subsec_time_original = subsec_time_original

    @property
    def user_comment(self):
        """Gets the user_comment of this ExifData.  # noqa: E501

        Gets or sets the user comment.  # noqa: E501

        :return: The user_comment of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._user_comment

    @user_comment.setter
    def user_comment(self, user_comment):
        """Sets the user_comment of this ExifData.

        Gets or sets the user comment.  # noqa: E501

        :param user_comment: The user_comment of this ExifData.  # noqa: E501
        :type: str
        """
        self._user_comment = user_comment

    @property
    def white_balance(self):
        """Gets the white_balance of this ExifData.  # noqa: E501

        Gets or sets the white balance.  # noqa: E501

        :return: The white_balance of this ExifData.  # noqa: E501
        :rtype: str
        """
        return self._white_balance

    @white_balance.setter
    def white_balance(self, white_balance):
        """Sets the white_balance of this ExifData.

        Gets or sets the white balance.  # noqa: E501

        :param white_balance: The white_balance of this ExifData.  # noqa: E501
        :type: str
        """
        self._white_balance = white_balance

    @property
    def white_point(self):
        """Gets the white_point of this ExifData.  # noqa: E501

        Gets or sets the white point.  # noqa: E501

        :return: The white_point of this ExifData.  # noqa: E501
        :rtype: list[float]
        """
        return self._white_point

    @white_point.setter
    def white_point(self, white_point):
        """Sets the white_point of this ExifData.

        Gets or sets the white point.  # noqa: E501

        :param white_point: The white_point of this ExifData.  # noqa: E501
        :type: list[float]
        """
        self._white_point = white_point

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data.get(self.discriminator)
        return self.discriminator_value_class_map.get(discriminator_value.lower()) if discriminator_value else None

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
        if not isinstance(other, ExifData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
