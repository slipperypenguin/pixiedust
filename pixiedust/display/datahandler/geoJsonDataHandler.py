# -------------------------------------------------------------------------------
# Copyright IBM Corp. 2017
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -------------------------------------------------------------------------------

import pandas
from pixiedust.utils import Logger
from .baseDataHandler import BaseDataHandler
import geojson

@Logger()
class GeoJSONDataHandler(BaseDataHandler):
    def __init__(self, options, entity):
        self.debug("Received a GeoJSON Entity")
        if not entity.is_valid:
            raise TypeError("Entity is not valid GeoJSON.")
        super(GeoJSONDataHandler, self).__init__(options, entity)


    def getFieldNames(self, expandNested=False):
        fieldNames = set();
        for feature in self.entity['features']:
            if 'properties' in feature:
                print(feature['properties'].keys())
                fieldNames.update(feature['properties'].keys())
        return fieldNames

    def isNumericField(self, fieldName):
        if fieldName in self.getFieldNames():
            for feature in self.entity['features']:
                if fieldName in feature:
                    print(feature[fieldName])
                    if not isinstance(feature[fieldName], (int, long, float, complex)):
                        return False
            return True
        else:
            raise ValueError("Property {} does not existing in the GeoJSON".format(fieldName))
