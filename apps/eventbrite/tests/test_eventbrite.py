# coding=utf-8
from django.test import TestCase
from requests import get
from django.conf import settings
from apps.meetup.models import Event


class EventbriteTest(TestCase):
    def test_api_token(self):
        response = get('https://www.eventbriteapi.com/v3/events/search/?',
            params={
                "token": settings.EVENTBRITE_OAUTH_KEY,
                "venue.city": "miami",
                "page": "1",
            }
        )
        self.assertEqual(response.status_code, 200)

    def test_save_event(self):
        from apps.eventbrite.management.commands.eventbrite import Command

        event_json = {
            "resource_uri": "https://www.eventbriteapi.com/v3/events/5911813393/",
            "name": {
                "text": "Certified Data Center Management Professional (CDCMP)",
                "html": "Certified Data Center Management Professional (CDCMP)"
            },
            "description": {
                "text": "Certified Data Center Management Professional (CDCMP) in Hong Kong, Macau and Great China \n  \nOverview  \nThe CDCMP course comprises a comprehensive program that explores and addresses all the various elements associated with managing a data centre – from understanding basic design principles and the physical infrastructure, to project management strategies and clear understanding the latest auditing tools. \n  \nPost Completion  \nAs well as achieving the prestigious CDCMP certification delegates will also receive the Level 5 BTEC Advanced Professional Award in Data Centre Management. \n   \nCourse Structure  \nThe CDCMP course is classroom based with numerous case study exercises and led by one of CNet Training’s expert instructors. It is divided into the following two units that can be taken independently in the following sequence: \n   \nCore Unit (3-day)  \nThis three-day course covers the essential elements of data centre management including design strategies and principles, project management delivery and managing the data centre with the use of applicable management tools. After completing the Core Unit delegates are awarded the CDCMP designation. \n  \n- Defining a Data Center \n- General Design Principles \n- Physical Infrastructure \n- Project Management \n- Managing the Data Centre \n- Management Tools \n   \nAdvanced Professional Unit (4-day)  \nThis four-day course comprises an in-depth analysis of the vital elements of data centre management – physical infrastructure components, business, operational and supporting strategies, compliance (National & International) and auditing. Topics such as management of processes, people and plant, business and IT strategies, and legislation and regulations are all covered.  \n  \n- Data Centre Physical \n- Data Centre Strategies \n- Data Centre Compliance \n- Data Centre Auditing \n  \nFor detai, please visit local website at http://www.stmedia-asia.com/cdcmp or download detailed syllabus at http://www.stmedia-asia.com/cdcmp/images/cdcmp.pdf \n  \nStrategic Media Asia (SMA) is an authorised regional agent of CNet Training, UK (www.cnet-training.com) in Hong Kong, Macau and Great China.",
                "html": "<P><SPAN STYLE=\"font-size: small;\"><STRONG><SPAN STYLE=\"text-decoration: underline;\">Certified Data Center Management Professional (CDCMP) in Hong Kong, Macau and Great China</SPAN></STRONG></SPAN></P>\r\n<P> </P>\r\n<P><STRONG>Overview </STRONG></P>\r\n<P>The CDCMP course comprises a comprehensive program that explores and addresses all the various elements associated with managing a data centre – from understanding basic design principles and the physical infrastructure, to project management strategies and clear understanding the latest auditing tools.</P>\r\n<P> </P>\r\n<P><STRONG>Post Completion </STRONG></P>\r\n<P>As well as achieving the prestigious CDCMP certification delegates will also receive the Level 5 BTEC Advanced Professional Award in Data Centre Management.</P>\r\n<P>  </P>\r\n<P><STRONG>Course Structure </STRONG></P>\r\n<P>The CDCMP course is classroom based with numerous case study exercises and led by one of CNet Training’s expert instructors. It is divided into the following two units that can be taken independently in the following sequence:</P>\r\n<P>  </P>\r\n<P><STRONG>Core Unit (3-day) </STRONG></P>\r\n<P>This three-day course covers the essential elements of data centre management including design strategies and principles, project management delivery and managing the data centre with the use of applicable management tools. After completing the Core Unit delegates are awarded the CDCMP designation.</P>\r\n<P> </P>\r\n<P>- Defining a Data Center</P>\r\n<P>- General Design Principles</P>\r\n<P>- Physical Infrastructure</P>\r\n<P>- Project Management</P>\r\n<P>- Managing the Data Centre</P>\r\n<P>- Management Tools</P>\r\n<P>  </P>\r\n<P><STRONG>Advanced Professional Unit (4-day) </STRONG></P>\r\n<P>This four-day course comprises an in-depth analysis of the vital elements of data centre management – physical infrastructure components, business, operational and supporting strategies, compliance (National & International) and auditing. Topics such as management of processes, people and plant, business and IT strategies, and legislation and regulations are all covered. </P>\r\n<P> </P>\r\n<P>- Data Centre Physical</P>\r\n<P>- Data Centre Strategies</P>\r\n<P>- Data Centre Compliance</P>\r\n<P>- Data Centre Auditing</P>\r\n<P> </P>\r\n<P>For detai, please visit local website at <A HREF=\"http://www.stmedia-asia.com/cdcmp\" REL=\"nofollow\">http://www.stmedia-asia.com/cdcmp</A> or download detailed syllabus at <A HREF=\"http://www.stmedia-asia.com/cdcmp/images/cdcmp.pdf\" REL=\"nofollow\">http://www.stmedia-asia.com/cdcmp/images/cdcmp.pdf</A></P>\r\n<P> </P>\r\n<P>Strategic Media Asia (SMA) is an authorised regional agent of CNet Training, UK (www.cnet-training.com) in Hong Kong, Macau and Great China.</P>"
            },
            "logo": {
                "id": "1319911",
                "url": "http://cdn.evbuc.com/images/1319911/55892607553/1/logo.jpg"
            },
            "id": "5911813393",
            "url": "http://cdcmp.eventbrite.hk/?aff=ebapi",
            "logo_url": "http://cdn.evbuc.com/images/1319911/55892607553/1/logo.jpg",
            "start": {
                "timezone": "Asia/Hong_Kong",
                "local": "2015-02-05T10:00:00",
                "utc": "2015-02-05T02:00:00Z"
            },
            "end": {
                "timezone": "Asia/Hong_Kong",
                "local": "2015-02-07T18:00:00",
                "utc": "2015-02-07T10:00:00Z"
            },
            "created": "2013-03-19T08:19:33Z",
            "changed": "2014-07-08T09:16:16Z",
            "capacity": 50,
            "status": "live",
            "currency": None,
            "online_event": None,
            "organizer_id": "3477029013",
            "venue_id": "3603961",
            "category_id": None,
            "subcategory_id": None,
            "format_id": "9",
            "organizer": {
                "description": {
                    "text": "Strategic Media Asia (www.stmedia-asia.com) is a leading technical training and event organizer for corporations specialized in ICT, telecommunication, management technologies and data center management, design and build. Currently, SMA delivers the following local seminars and data center events in Hong Kong and Macau.\r\nData Center Facilities Series\r\n\r\nData Center Facilities Design and Infrastructure Engineering (2-day)\r\nHVAC Design and Cooling Specialist for Data Center (2-day)\r\n\r\n \r\nWorldwide Accredited Data Center Qualifications\r\n\r\nCertified Data Center Design Professional (CDCDP, 7-day Course)\r\nCertified Data Center Management Professional (CDCMP, 7-day Course)\r\nRegistered Communications Distribution Designer (RCDD, 6-day Course)\r\n\r\n \r\nGreen Data Center Series\r\n\r\nGreen IT (ICT)\r\nEU Code of Conduct for Data Center Energy Efficiency\r\nEnergy and Cost Management for Data Center\r\n\r\n \r\nData Center Technical Visit / Site Tour\r\n \r\nAll these events / training seminars are designed to support the leadership needs of senior executives (Chief Information Officers, IT Directors / Managers, Facilities Managers, company decision makers, etc.) and to provide useful and applicable knowledge.\r\nOur experience speakers and consultants, combined with professional Chartered Engineers (CEng) from the Institute of Engineering Technology (IET), the Chartered Institute of Building Services Engineers (CIBSE) and the Hong Kong Institution of Engineers (HKIE), have more than 15 years experience in data centre design & build, energy conservation and facilities management in the private and public sectors.",
                    "html": "<P><SPAN><STRONG>Strategic Media Asia</STRONG> (<A HREF=\"http://www.stmedia-asia.com/\" TARGET=\"_blank\">www.stmedia-asia.com</A>) is a leading technical training and event organizer</SPAN><SPAN> for corporations specialized in ICT, telecommunication, management technologies and data center management, design and build. Currently, SMA delivers the following local seminars and data center events in Hong Kong and Macau.</SPAN></P>\r\n<P><BR><SPAN><STRONG>Data Center Facilities Series</STRONG></SPAN></P>\r\n<UL>\r\n<LI><A TITLE=\"Data Center Facilities Design and Infrastructure Engineering\" HREF=\"http://www.stmedia-asia.com/newsletter_6.html\" TARGET=\"_blank\">Data Center Facilities Design and Infrastructure Engineering</A> (2-day)</LI>\r\n<LI><A TITLE=\"HVAC Design & Cooling Specialist for Data Center\" HREF=\"http://www.stmedia-asia.com/newsletter_6.html\" TARGET=\"_blank\">HVAC Design and Cooling Specialist for Data Center</A> (2-day)</LI>\r\n</UL>\r\n<P><STRONG></STRONG> </P>\r\n<P><STRONG><SPAN>Worldwide Accredited Data Center Qualifications</SPAN></STRONG></P>\r\n<UL>\r\n<LI><A TITLE=\"Certified Data Center Design Professional CDCDP\" HREF=\"http://www.stmedia-asia.com/cdcdp/index.html\" TARGET=\"_blank\">Certified Data Center Design Professional</A> (CDCDP, 7-day Course)</LI>\r\n<LI><A TITLE=\"Certified Data Center Management Professional CDCMP\" HREF=\"http://www.stmedia-asia.com/cdcmp/index.html\" TARGET=\"_blank\">Certified Data Center Management Professional</A> (CDCMP, 7-day Course)</LI>\r\n<LI><A TITLE=\"Registered Communications Distribution Designer RCDD\" HREF=\"http://www.stmedia-asia.com/rcdd.html\" TARGET=\"_blank\">Registered Communications Distribution Designer</A> (RCDD, 6-day Course)</LI>\r\n</UL>\r\n<P> </P>\r\n<P><STRONG>Green Data Center Series</STRONG></P>\r\n<UL>\r\n<LI>Green IT (ICT)</LI>\r\n<LI>EU Code of Conduct for Data Center Energy Efficiency</LI>\r\n<LI>Energy and Cost Management for Data Center</LI>\r\n</UL>\r\n<P> </P>\r\n<P><A TITLE=\"Data Center Technical Visit / Site Tour\" HREF=\"http://www.stmedia-asia.com/data-center-tour.html\" TARGET=\"_blank\"><SPAN><STRONG>Data Center Technical Visit / Site Tour</STRONG></SPAN></A></P>\r\n<P> </P>\r\n<P>All these events / training seminars are designed to support the leadership needs of senior executives (Chief Information Officers, IT Directors / Managers, Facilities Managers, company decision makers, etc.) and to provide useful and applicable knowledge.</P>\r\n<P>Our experience speakers and consultants, combined with professional Chartered Engineers (CEng) from the Institute of Engineering Technology (IET), the Chartered Institute of Building Services Engineers (CIBSE) and the Hong Kong Institution of Engineers (HKIE), have more than 15 years experience in data centre design & build, energy conservation and facilities management in the private and public sectors.</P>"
                },
                "logo": {
                    "id": "1313253",
                    "url": "http://cdn.evbuc.com/images/1313253/55892607553/1/logo.jpg"
                },
                "resource_uri": "https://www.eventbriteapi.com/v3/organizers/3477029013/",
                "id": "3477029013",
                "name": "Strategic Media Asia",
                "url": "http://data-center.eventbrite.com",
                "num_past_events": 3,
                "num_future_events": 0
            },
            "venue": {
                "address": {
                    "address_1": "72 Tat Chee Avenue",
                    "address_2": None,
                    "city": "Kowloon Tong",
                    "region": None,
                    "postal_code": None,
                    "country": "HK"
                },
                "resource_uri": "https://www.eventbriteapi.com/v3/venues/3603961/",
                "id": "3603961",
                "name": "Innocentre Hong Kong",
                "latitude": "22.33535",
                "longitude": "114.17611099999999"
            },
            "category": None,
            "subcategory": None,
            "format": {
                "resource_uri": "https://www.eventbriteapi.com/v3/formats/9/",
                "id": "9",
                "name": "Class, Training, or Workshop",
                "short_name": "Class"
            },
            "ticket_classes": [
                {
                    "resource_uri": "https://www.eventbriteapi.com/v3/events/5911813393/ticket_classes/17768365/",
                    "id": "17768365",
                    "name": "CDCMP (Core Unit, 3-day)",
                    "description": None,
                    "cost": {
                        "currency": "HKD",
                        "display": "17500.00 HKD",
                        "value": 1750000
                    },
                    "fee": {
                        "currency": "HKD",
                        "display": "77.50 HKD",
                        "value": 7750
                    },
                    "donation": False,
                    "free": False,
                    "minimum_quantity": 1,
                    "maximum_quantity": None,
                    "variants": [],
                    "event_id": "5911813393"
                }
            ]
        }

        Command.save_event_from_json(event_json)
        self.assertEqual(Event.objects.count(), 1)

        # Make sure that it does not import a duplicate record.
        event_json['name']['text'] = "Test Event"
        Command.save_event_from_json(event_json)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Event.objects.first().event_name, "Test Event")