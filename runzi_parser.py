import gpxpy
import gpxpy.gpx
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
        gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(point.lat, point.long, elevation=1234))

    # You can add routes and waypoints, too...

    print 'Created GPX:', gpx.to_xml()


def export_runzi_points(file_obj, time=datetime.now()):
    runzi_list = []
    current_time = time
    for line in file_obj.readlines()[3:]:
        indv_point = line.split('|')
        current_time += timedelta(0, int(indv_point[0]))
        runzi_point = {
            'latitude': indv_point[2],
            'longitude': indv_point[3],
            'time': current_time
        }
        runzi_list.append(runzi_point)
    return runzi_list
