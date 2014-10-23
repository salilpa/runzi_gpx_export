import gpxpy
import gpxpy.gpx
import srtm
from datetime import datetime, timedelta


def gpx_create(list_of_runzi_points, name):
    # Creating a new file:
    # --------------------

    gpx = gpxpy.gpx.GPX()

    # Create first track in our GPX:
    gpx_track = gpxpy.gpx.GPXTrack()
    gpx_track.name = name
    gpx.tracks.append(gpx_track)

    # Create first segment in our GPX track:
    gpx_segment = gpxpy.gpx.GPXTrackSegment()
    gpx_track.segments.append(gpx_segment)

    for point in list_of_runzi_points:
        gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(point['latitude'], point['longitude'], time=point['time'],
                                                          elevation=point['elevation']))

    # You can add routes and waypoints, too...

    return gpx.to_xml()


def export_runzi_points(file_obj, time=datetime.now()):
    runzi_list = []
    elevation_data = srtm.get_data()
    current_time = time - timedelta(hours=10)
    for line in file_obj.readlines()[3:]:
        indv_point = line.split('|')
        current_time += timedelta(0, milliseconds=int(indv_point[0]))
        runzi_point = {
            'latitude': indv_point[2],
            'longitude': indv_point[3],
            'time': current_time,
            'elevation': elevation_data.get_elevation(indv_point[2], indv_point[3])
        }
        runzi_list.append(runzi_point)
    return runzi_list


file_obj = open('test_files/runzi_file.txt')
objects = export_runzi_points(file_obj)
gpx_obj = gpx_create(objects, 'test run')
output_file = open('test_files/output.gpx', 'w')
output_file.write(gpx_obj)
file_obj.close()
output_file.close()
