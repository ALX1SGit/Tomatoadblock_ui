#/usr/bin/python
#from flask import Flask, render_template, request, redirect, url_for, flash
#import system
from flask import Flask, render_template, flash, url_for
import subprocess
import shlex
import datetime
from time import strptime
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Getting Devices Name
def device_list():
	usr= 'root'
	password= 'laylasaurio'
	router = "192.168.1.1"
	queryStr1 = 'http://' + router + '/status-devices.asp'
	r1 = requests.get(queryStr1, auth=(usr, password), verify=False)
	dhcpd_lease=str(r1.text).split("dhcpd_lease = ")[1].split(";")[0].replace("[ [","").replace("]]","").split("],[")
	return dhcpd_lease

#for testing in Windows
out="""b'Jun 24 09:56:02 unknown daemon.info dnsmasq[2743]: reply ngep.blackspider.com is                                                             <CNAME>
Jun 24 09:56:02 unknown daemon.info dnsmasq[2743]: reply iq.global.websense.net                                                             is 208.87.234.169
Jun 24 09:56:02 unknown daemon.info dnsmasq[2743]: query[A] googleads.g.doublecl                                                            ick.net from 192.168.1.35
Jun 24 09:56:02 unknown daemon.info dnsmasq[2743]: config googleads.g.doubleclic                                                            k.net is 0.0.0.0
Jun 24 09:56:02 unknown daemon.info dnsmasq[2743]: query[A] beacons.gcp.gvt2.com                                                             from 192.168.1.35
Jun 24 09:56:02 unknown daemon.info dnsmasq[2743]: config beacons.gcp.gvt2.com i                                                            s 0.0.0.0
Jun 24 09:56:02 unknown daemon.info dnsmasq[2743]: query[A] beacons.gcp.gvt2.com                                                             from 192.168.1.35
Jun 24 09:56:02 unknown daemon.info dnsmasq[2743]: config beacons.gcp.gvt2.com i                                                            s 0.0.0.0
Jun 24 09:56:02 unknown daemon.info dnsmasq[2743]: query[A] beacons.gvt2.com fro                                                            m 192.168.1.35
Jun 24 09:56:02 unknown daemon.info dnsmasq[2743]: config beacons.gvt2.com is 0.                                                            0.0.0
Jun 24 09:56:02 unknown daemon.info dnsmasq[2743]: query[A] beacons.gvt2.com fro                                                            m 192.168.1.35
Jun 24 09:56:03 unknown daemon.info dnsmasq[2743]: config beacons.gvt2.com is 0.                                                            0.0.0
Jun 24 09:56:03 unknown daemon.info dnsmasq[2743]: query[A] beacons.gvt2.com fro                                                            m 192.168.1.35
Jun 24 09:56:03 unknown daemon.info dnsmasq[2743]: config beacons.gvt2.com is 0.                                                            0.0.0
Jun 24 09:56:03 unknown daemon.info dnsmasq[2743]: query[A] beacons.gvt2.com fro                                                            m 192.168.1.35
Jun 24 09:56:03 unknown daemon.info dnsmasq[2743]: config beacons.gvt2.com is 0.                                                            0.0.0
Jun 24 09:56:03 unknown daemon.info dnsmasq[2743]: query[A] beacons.gvt2.com fro                                                            m 192.168.1.35
Jun 24 09:56:03 unknown daemon.info dnsmasq[2743]: config beacons.gvt2.com is 0.                                                            0.0.0
Jun 24 09:56:03 unknown daemon.info dnsmasq[2743]: query[A] beacons.gcp.gvt2.com                                                             from 192.168.1.35
Jun 24 09:56:03 unknown daemon.info dnsmasq[2743]: config beacons.gcp.gvt2.com i                                                            s 0.0.0.0
Jun 24 09:56:03 unknown daemon.info dnsmasq[2743]: query[A] wpad.accenture.com f                                                            rom 192.168.1.35
Jun 24 09:56:03 unknown daemon.info dnsmasq[2743]: cached wpad.accenture.com is                                                             NXDOMAIN
Jun 24 09:56:10 unknown daemon.info dnsmasq[2743]: query[A] wpad.accenture.com f                                                            rom 192.168.1.35
Jun 24 09:56:10 unknown daemon.info dnsmasq[2743]: cached wpad.accenture.com is                                                             NXDOMAIN
Jun 24 09:56:15 unknown daemon.info dnsmasq[2743]: query[A] presence.teams.micro                                                            soft.com from 192.168.1.35
Jun 24 09:56:15 unknown daemon.info dnsmasq[2743]: cached presence.teams.microso                                                            ft.com is <CNAME>
Jun 24 09:56:15 unknown daemon.info dnsmasq[2743]: cached presence.services.sfb.                                                            trafficmanager.net is <CNAME>
Jun 24 09:56:15 unknown daemon.info dnsmasq[2743]: forwarded presence.teams.micr                                                            osoft.com to 8.8.8.8
Jun 24 09:56:15 unknown daemon.info dnsmasq[2743]: reply presence.teams.microsof                                                            t.com is <CNAME>
Jun 24 09:56:15 unknown daemon.info dnsmasq[2743]: reply presence.services.sfb.t                                                            rafficmanager.net is <CNAME>
Jun 24 09:56:15 unknown daemon.info dnsmasq[2743]: reply a-ups-presence13-prod-a                                                            zsc.centralus.cloudapp.azure.com is 52.112.113.24
Jun 24 09:56:16 unknown daemon.info dnsmasq[2743]: query[A] mail.google.com from                                                             192.168.1.35
Jun 24 09:56:16 unknown daemon.info dnsmasq[2743]: cached mail.google.com is <CN                                                            AME>
Jun 24 09:56:16 unknown daemon.info dnsmasq[2743]: forwarded mail.google.com to                                                             8.8.8.8
Jun 24 09:56:16 unknown daemon.info dnsmasq[2743]: reply mail.google.com is <CNA                                                            ME>
Jun 24 09:56:16 unknown daemon.info dnsmasq[2743]: reply googlemail.l.google.com                                                             is 172.217.172.37
Jun 24 09:56:25 unknown daemon.info dnsmasq[2743]: query[A] self.events.data.mic                                                            rosoft.com from 192.168.1.35
Jun 24 09:56:25 unknown daemon.info dnsmasq[2743]: cached self.events.data.micro                                                            soft.com is <CNAME>
Jun 24 09:56:25 unknown daemon.info dnsmasq[2743]: forwarded self.events.data.mi                                                            crosoft.com to 8.8.8.8
Jun 24 09:56:25 unknown daemon.info dnsmasq[2743]: forwarded self.events.data.mi                                                            crosoft.com to 8.8.4.4
Jun 24 09:56:25 unknown daemon.info dnsmasq[2743]: reply self.events.data.micros                                                            oft.com is <CNAME>
Jun 24 09:56:25 unknown daemon.info dnsmasq[2743]: reply self-events-data.traffi                                                            cmanager.net is <CNAME>
Jun 24 09:56:25 unknown daemon.info dnsmasq[2743]: reply skypedataprdcolweu03.cl                                                            oudapp.net is 52.114.74.44
Jun 24 09:56:29 unknown daemon.info dnsmasq[2743]: query[A] eu-v20.events.data.m                                                            icrosoft.com from 192.168.1.35
Jun 24 09:56:29 unknown daemon.info dnsmasq[2743]: cached eu-v20.events.data.mic                                                            rosoft.com is <CNAME>
Jun 24 09:56:29 unknown daemon.info dnsmasq[2743]: forwarded eu-v20.events.data.                                                            microsoft.com to 8.8.8.8
Jun 24 09:56:29 unknown daemon.info dnsmasq[2743]: reply eu-v20.events.data.micr                                                            osoft.com is <CNAME>
Jun 24 09:56:29 unknown daemon.info dnsmasq[2743]: reply eu.events.data.trafficm                                                            anager.net is <CNAME>
Jun 24 09:56:29 unknown daemon.info dnsmasq[2743]: reply skypedataprdcolweu06.cl                                                            oudapp.net is 52.114.75.150
Jun 24 09:56:38 unknown daemon.info dnsmasq[2743]: query[A] a03cmg01.accenture.c                                                            om from 192.168.1.35
Jun 24 09:56:38 unknown daemon.info dnsmasq[2743]: cached a03cmg01.accenture.com                                                             is <CNAME>
Jun 24 09:56:38 unknown daemon.info dnsmasq[2743]: forwarded a03cmg01.accenture.                                                            com to 8.8.8.8
Jun 24 09:56:38 unknown daemon.info dnsmasq[2743]: reply a03cmg01.accenture.com                                                             is <CNAME>
Jun 24 09:56:38 unknown daemon.info dnsmasq[2743]: reply a03cmg01.cloudapp.net i                                                            s 23.96.114.53
Jun 24 09:56:41 unknown daemon.info dnsmasq[2743]: query[A] beacons.gcp.gvt2.com                                                             from 192.168.1.35
Jun 24 09:56:41 unknown daemon.info dnsmasq[2743]: config beacons.gcp.gvt2.com i                                                            s 0.0.0.0
Jun 24 09:56:43 unknown daemon.info dnsmasq[2743]: query[A] www.facebook.com fro                                                            m 192.168.1.35
Jun 24 09:56:43 unknown daemon.info dnsmasq[2743]: forwarded www.facebook.com to                                                             8.8.8.8
Jun 24 09:56:43 unknown daemon.info dnsmasq[2743]: reply www.facebook.com is <CN                                                            AME>
Jun 24 09:56:43 unknown daemon.info dnsmasq[2743]: reply star-mini.c10r.facebook                                                            .com is 31.13.94.35
Jun 24 09:56:43 unknown daemon.info dnsmasq[2743]: query[A] scontent.faep9-2.fna                                                            .fbcdn.net from 192.168.1.35
Jun 24 09:56:43 unknown daemon.info dnsmasq[2743]: forwarded scontent.faep9-2.fn                                                            a.fbcdn.net to 8.8.8.8
Jun 24 09:56:43 unknown daemon.info dnsmasq[2743]: query[A] scontent.faep9-1.fna                                                            .fbcdn.net from 192.168.1.35
Jun 24 09:56:43 unknown daemon.info dnsmasq[2743]: forwarded scontent.faep9-1.fn                                                            a.fbcdn.net to 8.8.8.8
Jun 24 09:56:43 unknown daemon.info dnsmasq[2743]: reply scontent.faep9-2.fna.fb                                                            cdn.net is 181.30.193.81
Jun 24 09:56:43 unknown daemon.info dnsmasq[2743]: reply scontent.faep9-1.fna.fb                                                            cdn.net is 181.30.193.17
Jun 24 09:56:43 unknown daemon.info dnsmasq[2743]: query[A] beacons.gvt2.com fro                                                            m 192.168.1.35
Jun 24 09:56:43 unknown daemon.info dnsmasq[2743]: config beacons.gvt2.com is 0.                                                            0.0.0
Jun 24 09:56:43 unknown daemon.info dnsmasq[2743]: query[A] beacons.gvt2.com fro                                                            m 192.168.1.35
Jun 24 09:56:43 unknown daemon.info dnsmasq[2743]: config beacons.gvt2.com is 0.                                                            0.0.0
Jun 24 09:57:03 unknown daemon.info dnsmasq[2743]: query[A] beacons3.gvt2.com fr                                                            om 192.168.1.35
Jun 24 09:57:03 unknown daemon.info dnsmasq[2743]: forwarded beacons3.gvt2.com t                                                            o 8.8.8.8
Jun 24 09:57:03 unknown daemon.info dnsmasq[2743]: forwarded beacons3.gvt2.com t                                                            o 8.8.4.4
Jun 24 09:57:03 unknown daemon.info dnsmasq[2743]: reply beacons3.gvt2.com is 17                                                            2.217.172.163
Jun 24 09:57:05 unknown daemon.info dnsmasq[2743]: query[A] ssl.google-analytics                                                            .com from 192.168.1.132
Jun 24 09:57:05 unknown daemon.info dnsmasq[2743]: config ssl.google-analytics.c                                                            om is 0.0.0.0
Jun 24 09:57:12 unknown daemon.info dnsmasq[2743]: query[A] wpad.accenture.com f                                                            rom 192.168.1.35
Jun 24 09:57:12 unknown daemon.info dnsmasq[2743]: cached wpad.accenture.com is                                                             NXDOMAIN
Jun 24 09:57:20 unknown daemon.info dnsmasq[2743]: query[A] fonts.gstatic.com fr                                                            om 192.168.1.35
Jun 24 09:57:20 unknown daemon.info dnsmasq[2743]: forwarded fonts.gstatic.com t                                                            o 8.8.8.8
Jun 24 09:57:20 unknown daemon.info dnsmasq[2743]: reply fonts.gstatic.com is <C                                                            NAME>
Jun 24 09:57:20 unknown daemon.info dnsmasq[2743]: reply gstaticadssl.l.google.c                                                            om is 64.233.190.94
Jun 24 09:57:25 unknown daemon.info dnsmasq[2743]: query[A] appslosrios-my.share                                                            point.com from 192.168.1.35
Jun 24 09:57:25 unknown daemon.info dnsmasq[2743]: cached appslosrios-my.sharepo                                                            int.com is <CNAME>
Jun 24 09:57:25 unknown daemon.info dnsmasq[2743]: cached appslosrios.sharepoint                                                            .com is <CNAME>
Jun 24 09:57:25 unknown daemon.info dnsmasq[2743]: forwarded appslosrios-my.shar                                                            epoint.com to 8.8.8.8
Jun 24 09:57:25 unknown daemon.info dnsmasq[2743]: forwarded appslosrios-my.shar                                                            epoint.com to 8.8.4.4
Jun 24 09:57:26 unknown daemon.info dnsmasq[2743]: reply appslosrios-my.sharepoi                                                            nt.com is <CNAME>
Jun 24 09:57:26 unknown daemon.info dnsmasq[2743]: reply appslosrios.sharepoint.                                                            com is <CNAME>
Jun 24 09:57:26 unknown daemon.info dnsmasq[2743]: reply 41-ipv4e.clump.dprodmgd                                                            105.aa-rt.sharepoint.com is <CNAME>
Jun 24 09:57:26 unknown daemon.info dnsmasq[2743]: reply 191092-ipv4e.farm.dprod                                                            mgd105.aa-rt.sharepoint.com is <CNAME>
Jun 24 09:57:26 unknown daemon.info dnsmasq[2743]: reply 191092-ipv4e.farm.dprod                                                            mgd105.sharepointonline.com.akadns.net is <CNAME>
Jun 24 09:57:26 unknown daemon.info dnsmasq[2743]: reply 191092-ipv4.farm.dprodm                                                            gd105.aa-rt.sharepoint.com.spo-0004.spo-msedge.net is <CNAME>
Jun 24 09:57:26 unknown daemon.info dnsmasq[2743]: reply spo-0004.spo-msedge.net                                                             is 13.107.136.9
Jun 24 09:57:27 unknown daemon.info dnsmasq[2743]: query[A] web.whatsapp.com fro                                                            m 192.168.1.35
Jun 24 09:57:27 unknown daemon.info dnsmasq[2743]: forwarded web.whatsapp.com to                                                             8.8.4.4
Jun 24 09:57:27 unknown daemon.info dnsmasq[2743]: reply web.whatsapp.com is <CN                                                            AME>
Jun 24 09:57:27 unknown daemon.info dnsmasq[2743]: reply mmx-ds.cdn.whatsapp.net                                                             is 31.13.94.52
Jun 24 09:57:28 unknown daemon.info dnsmasq[2743]: query[A] beacons.gcp.gvt2.com                                                             from 192.168.1.35
Jun 24 09:57:28 unknown daemon.info dnsmasq[2743]: config beacons.gcp.gvt2.com i                                                            s 0.0.0.0
Jun 24 09:57:31 unknown daemon.info dnsmasq[2743]: query[A] self.events.data.mic                                                            rosoft.com from 192.168.1.35
Jun 24 09:57:31 unknown daemon.info dnsmasq[2743]: cached self.events.data.micro                                                            soft.com is <CNAME>
Jun 24 09:57:31 unknown daemon.info dnsmasq[2743]: forwarded self.events.data.mi                                                            crosoft.com to 8.8.4.4
Jun 24 09:57:31 unknown daemon.info dnsmasq[2743]: reply self.events.data.micros                                                            oft.com is <CNAME>
Jun 24 09:57:31 unknown daemon.info dnsmasq[2743]: reply self-events-data.traffi                                                            cmanager.net is <CNAME>
Jun 24 09:57:31 unknown daemon.info dnsmasq[2743]: reply skypedataprdcolcus01.cl                                                            oudapp.net is 52.114.128.75
Jun 24 09:57:31 unknown daemon.info dnsmasq[2743]: query[A] stage-ipam.accenture                                                            .com from 192.168.1.35
Jun 24 09:57:31 unknown daemon.info dnsmasq[2743]: cached stage-ipam.accenture.c                                                            om is NXDOMAIN
Jun 24 09:57:31 unknown daemon.info dnsmasq[2743]: query[A] chins1901.accenture.                                                            com from 192.168.1.35
Jun 24 09:57:31 unknown daemon.info dnsmasq[2743]: forwarded chins1901.accenture                                                            .com to 8.8.4.4
Jun 24 09:57:31 unknown daemon.info dnsmasq[2743]: query[A] myapps.shire.com fro                                                            m 192.168.1.35
Jun 24 09:57:31 unknown daemon.info dnsmasq[2743]: cached myapps.shire.com is <C                                                            NAME>
Jun 24 09:57:31 unknown daemon.info dnsmasq[2743]: forwarded myapps.shire.com to                                                             8.8.4.4
Jun 24 09:57:31 unknown daemon.warn dnsmasq[2743]: possible DNS-rebind attack de                                                            tected: chins1901.accenture.com
Jun 24 09:57:31 unknown daemon.info dnsmasq[2743]: query[AAAA] chins1901.accentu                                                            re.com from 192.168.1.35
Jun 24 09:57:31 unknown daemon.info dnsmasq[2743]: cached chins1901.accenture.co                                                            m is NODATA-IPv6
Jun 24 09:57:31 unknown daemon.info dnsmasq[2743]: reply myapps.shire.com is <CN                                                            AME>
Jun 24 09:57:31 unknown daemon.info dnsmasq[2743]: reply gslb-ext.shire.com is 1                                                            95.216.225.94
Jun 24 09:57:31 unknown daemon.info dnsmasq[2743]: query[A] gslb-ext.shire.com f                                                            rom 192.168.1.35
Jun 24 09:57:31 unknown daemon.info dnsmasq[2743]: cached gslb-ext.shire.com is                                                             195.216.225.94
Jun 24 09:57:31 unknown daemon.info dnsmasq[2743]: query[AAAA] gslb-ext.shire.co                                                            m from 192.168.1.35
Jun 24 09:57:31 unknown daemon.info dnsmasq[2743]: forwarded gslb-ext.shire.com                                                             to 8.8.4.4
Jun 24 09:57:32 unknown daemon.info dnsmasq[2743]: query[A] da2-iod.accenture.co                                                            m from 192.168.1.35
Jun 24 09:57:32 unknown daemon.info dnsmasq[2743]: cached da2-iod.accenture.com                                                             is NXDOMAIN
Jun 24 09:57:32 unknown daemon.info dnsmasq[2743]: query[AAAA] gslb-ext.shire.co                                                            m from 192.168.1.35
Jun 24 09:57:32 unknown daemon.info dnsmasq[2743]: forwarded gslb-ext.shire.com                                                             to 8.8.8.8
Jun 24 09:57:32 unknown daemon.info dnsmasq[2743]: forwarded gslb-ext.shire.com                                                             to 8.8.4.4
Jun 24 09:57:33 unknown daemon.info dnsmasq[2743]: query[A] wpad.accenture.com f                                                            rom 192.168.1.35
Jun 24 09:57:33 unknown daemon.info dnsmasq[2743]: cached wpad.accenture.com is                                                             NXDOMAIN
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: query[A] incoming.telemetry.m                                                            ozilla.org from 192.168.1.35
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: forwarded incoming.telemetry.                                                            mozilla.org to 8.8.8.8
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: reply incoming.telemetry.mozi                                                            lla.org is <CNAME>
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: reply telemetry-incoming.r53-                                                            2.services.mozilla.com is <CNAME>
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: reply prod.data-ingestion.pro                                                            d.dataops.mozgcp.net is 35.244.247.133
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: query[A] prod.data-ingestion.                                                            prod.dataops.mozgcp.net from 192.168.1.35
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: cached prod.data-ingestion.pr                                                            od.dataops.mozgcp.net is 35.244.247.133
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: query[AAAA] prod.data-ingesti                                                            on.prod.dataops.mozgcp.net from 192.168.1.35
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: forwarded prod.data-ingestion                                                            .prod.dataops.mozgcp.net to 8.8.8.8
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: reply prod.data-ingestion.pro                                                            d.dataops.mozgcp.net is NODATA-IPv6
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: query[A] wiki.mozilla.org fro                                                            m 192.168.1.35
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: forwarded wiki.mozilla.org to                                                             8.8.8.8
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: query[A] support.mozilla.org                                                             from 192.168.1.35
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: forwarded support.mozilla.org                                                             to 8.8.8.8
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: query[A] www.mozilla.org from                                                             192.168.1.35
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: forwarded www.mozilla.org to                                                             8.8.8.8
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: reply support.mozilla.org is                                                             <CNAME>
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: reply prod-tp.sumo.mozit.clou                                                            d is 54.218.9.103
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: reply prod-tp.sumo.mozit.clou                                                            d is 44.227.102.134
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: query[A] prod-tp.sumo.mozit.c                                                            loud from 192.168.1.35
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: cached prod-tp.sumo.mozit.clo                                                            ud is 44.227.102.134
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: cached prod-tp.sumo.mozit.clo                                                            ud is 54.218.9.103
Jun 24 09:57:34 unknown daemon.info dnsmasq[2743]: query[AAAA] prod-tp.sumo.mozi                                                            t.cloud from 192.168.1.35
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: forwarded prod-tp.sumo.mozit.                                                            cloud to 8.8.8.8
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: reply wiki.mozilla.org is <CN                                                            AME>
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: reply wiki-prod-1394614349.us                                                            -west-2.elb.amazonaws.com is 34.209.101.174
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: reply wiki-prod-1394614349.us                                                            -west-2.elb.amazonaws.com is 52.37.70.70
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: reply wiki-prod-1394614349.us                                                            -west-2.elb.amazonaws.com is 44.231.199.58
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: query[A] wiki-prod-1394614349                                                            .us-west-2.elb.amazonaws.com from 192.168.1.35
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: cached wiki-prod-1394614349.u                                                            s-west-2.elb.amazonaws.com is 44.231.199.58
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: cached wiki-prod-1394614349.u                                                            s-west-2.elb.amazonaws.com is 52.37.70.70
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: cached wiki-prod-1394614349.u                                                            s-west-2.elb.amazonaws.com is 34.209.101.174
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: query[AAAA] wiki-prod-1394614                                                            349.us-west-2.elb.amazonaws.com from 192.168.1.35
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: forwarded wiki-prod-139461434                                                            9.us-west-2.elb.amazonaws.com to 8.8.8.8
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: reply prod-tp.sumo.mozit.clou                                                            d is NODATA-IPv6
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: reply www.mozilla.org is <CNA                                                            ME>
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: reply www.mozilla.org.cdn.clo                                                            udflare.net is 104.18.165.34
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: reply www.mozilla.org.cdn.clo                                                            udflare.net is 104.18.164.34
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: query[A] www.mozilla.org.cdn.                                                            cloudflare.net from 192.168.1.35
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: cached www.mozilla.org.cdn.cl                                                            oudflare.net is 104.18.164.34
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: cached www.mozilla.org.cdn.cl                                                            oudflare.net is 104.18.165.34
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: query[AAAA] www.mozilla.org.c                                                            dn.cloudflare.net from 192.168.1.35
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: forwarded www.mozilla.org.cdn                                                            .cloudflare.net to 8.8.8.8
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: reply www.mozilla.org.cdn.clo                                                            udflare.net is 2606:4700::6812:a522
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: reply www.mozilla.org.cdn.clo                                                            udflare.net is 2606:4700::6812:a422
Jun 24 09:57:35 unknown daemon.info dnsmasq[2743]: reply wiki-prod-1394614349.us                                                            -west-2.elb.amazonaws.com is NODATA-IPv6
Jun 24 09:57:45 unknown daemon.info dnsmasq[2743]: query[A] fonts.googleapis.com                                                             from 192.168.1.35
Jun 24 09:57:45 unknown daemon.info dnsmasq[2743]: forwarded fonts.googleapis.co                                                            m to 8.8.8.8
Jun 24 09:57:45 unknown daemon.info dnsmasq[2743]: reply fonts.googleapis.com is                                                             172.217.172.74
Jun 24 09:57:45 unknown daemon.info dnsmasq[2743]: query[A] fonts.googleapis.com                                                             from 192.168.1.35
Jun 24 09:57:45 unknown daemon.info dnsmasq[2743]: cached fonts.googleapis.com i                                                            s 172.217.172.74
Jun 24 09:57:45 unknown daemon.info dnsmasq[2743]: query[AAAA] fonts.googleapis.                                                            com from 192.168.1.35
Jun 24 09:57:45 unknown daemon.info dnsmasq[2743]: forwarded fonts.googleapis.co                                                            m to 8.8.8.8
Jun 24 09:57:45 unknown daemon.info dnsmasq[2743]: reply fonts.googleapis.com is                                                             2800:3f0:4002:802::200a
Jun 24 09:57:48 unknown daemon.info dnsmasq[2743]: query[A] wpad.accenture.com f                                                            rom 192.168.1.35
Jun 24 09:57:48 unknown daemon.info dnsmasq[2743]: cached wpad.accenture.com is                                                             NXDOMAIN
Jun 24 09:58:02 unknown daemon.info dnsmasq[2743]: query[A] winatp-gw-neu.micros                                                            oft.com from 192.168.1.35
Jun 24 09:58:02 unknown daemon.info dnsmasq[2743]: cached winatp-gw-neu.microsof                                                            t.com is <CNAME>
Jun 24 09:58:02 unknown daemon.info dnsmasq[2743]: forwarded winatp-gw-neu.micro                                                            soft.com to 8.8.8.8
Jun 24 09:58:02 unknown daemon.info dnsmasq[2743]: forwarded winatp-gw-neu.micro                                                            soft.com to 8.8.4.4
Jun 24 09:58:02 unknown daemon.info dnsmasq[2743]: reply winatp-gw-neu.microsoft                                                            .com is <CNAME>
Jun 24 09:58:02 unknown daemon.info dnsmasq[2743]: reply sevillecloudgateway-neu                                                            -prd.trafficmanager.net is <CNAME>
Jun 24 09:58:02 unknown daemon.info dnsmasq[2743]: reply wdatpprd-neu.securityce                                                            nter.windows.com is <CNAME>
Jun 24 09:58:02 unknown daemon.info dnsmasq[2743]: reply k8stm-prd-neu.trafficma                                                            nager.net is <CNAME>
Jun 24 09:58:02 unknown daemon.info dnsmasq[2743]: reply wdatp-prd-neu-6.northeu                                                            rope.cloudapp.azure.com is 137.135.216.188
Jun 24 09:58:02 unknown daemon.info dnsmasq[2743]: query[A] googleads.g.doublecl                                                            ick.net from 192.168.1.35
Jun 24 09:58:02 unknown daemon.info dnsmasq[2743]: config googleads.g.doubleclic                                                            k.net is 0.0.0.0
Jun 24 09:58:03 unknown daemon.info dnsmasq[2743]: query[A] beacons.gvt2.com fro                                                            m 192.168.1.35
Jun 24 09:58:03 unknown daemon.info dnsmasq[2743]: config beacons.gvt2.com is 0.                                                            0.0.0
Jun 24 09:58:03 unknown daemon.info dnsmasq[2743]: query[A] beacons.gvt2.com fro                                                            m 192.168.1.35
Jun 24 09:58:03 unknown daemon.info dnsmasq[2743]: config beacons.gvt2.com is 0.                                                            0.0.0
Jun 24 09:58:03 unknown daemon.info dnsmasq[2743]: query[A] clients2.google.com                                                             from 192.168.1.35
Jun 24 09:58:03 unknown daemon.info dnsmasq[2743]: forwarded clients2.google.com                                                             to 8.8.8.8
Jun 24 09:58:03 unknown daemon.info dnsmasq[2743]: query[A] beacons.gvt2.com fro                                                            m 192.168.1.35
Jun 24 09:58:03 unknown daemon.info dnsmasq[2743]: config beacons.gvt2.com is 0.                                                            0.0.0
Jun 24 09:58:03 unknown daemon.info dnsmasq[2743]: query[A] beacons.gvt2.com fro                                                            m 192.168.1.35
Jun 24 09:58:03 unknown daemon.info dnsmasq[2743]: config beacons.gvt2.com is 0.                                                            0.0.0
Jun 24 09:58:03 unknown daemon.info dnsmasq[2743]: reply clients2.google.com is                                                             <CNAME>
Jun 24 09:58:03 unknown daemon.info dnsmasq[2743]: reply clients.l.google.com is                                                             172.217.172.238
Jun 24 09:58:04 unknown daemon.info dnsmasq[2743]: query[A] da2-iod.accenture.co                                                            m from 192.168.1.35
Jun 24 09:58:04 unknown daemon.info dnsmasq[2743]: cached da2-iod.accenture.com                                                             is NXDOMAIN
Jun 24 09:58:05 unknown daemon.info dnsmasq[2743]: query[A] wpad.accenture.com f                                                            rom 192.168.1.35
Jun 24 09:58:05 unknown daemon.info dnsmasq[2743]: cached wpad.accenture.com is                                                             NXDOMAIN
Jun 24 09:58:20 unknown daemon.info dnsmasq[2743]: query[A] wpad.accenture.com f                                                            rom 192.168.1.35
Jun 24 09:58:20 unknown daemon.info dnsmasq[2743]: cached wpad.accenture.com is                                                             NXDOMAIN
Jun 24 09:58:25 unknown daemon.info dnsmasq[2743]: query[A] self.events.data.mic                                                            rosoft.com from 192.168.1.35
Jun 24 09:58:25 unknown daemon.info dnsmasq[2743]: cached self.events.data.micro                                                            soft.com is <CNAME>
Jun 24 09:58:25 unknown daemon.info dnsmasq[2743]: forwarded self.events.data.mi                                                            crosoft.com to 8.8.8.8
Jun 24 09:58:25 unknown daemon.info dnsmasq[2743]: forwarded self.events.data.mi                                                            crosoft.com to 8.8.4.4
Jun 24 09:58:25 unknown daemon.info dnsmasq[2743]: reply self.events.data.micros                                                            oft.com is <CNAME>
Jun 24 09:58:25 unknown daemon.info dnsmasq[2743]: reply self-events-data.traffi                                                            cmanager.net is <CNAME>
Jun 24 09:58:25 unknown daemon.info dnsmasq[2743]: reply skypedataprdcolcus02.cl                                                            oudapp.net is 52.114.128.9
Jun 24 09:58:30 unknown daemon.info dnsmasq[2743]: query[A] eu-v20.events.data.m                                                            icrosoft.com from 192.168.1.35
Jun 24 09:58:30 unknown daemon.info dnsmasq[2743]: cached eu-v20.events.data.mic                                                            rosoft.com is <CNAME>
Jun 24 09:58:30 unknown daemon.info dnsmasq[2743]: forwarded eu-v20.events.data.                                                            microsoft.com to 8.8.8.8
Jun 24 09:58:31 unknown daemon.info dnsmasq[2743]: reply eu-v20.events.data.micr                                                            osoft.com is <CNAME>
Jun 24 09:58:31 unknown daemon.info dnsmasq[2743]: reply eu.events.data.trafficm                                                            anager.net is <CNAME>
Jun 24 09:58:31 unknown daemon.info dnsmasq[2743]: reply skypedataprdcolweu04.cl                                                            oudapp.net is 52.114.75.78
Jun 24 09:58:42 unknown daemon.info dnsmasq[2743]: query[A] storeedgefd.dsx.mp.m                                                            icrosoft.com from 192.168.1.35
Jun 24 09:58:42 unknown daemon.info dnsmasq[2743]: forwarded storeedgefd.dsx.mp.                                                            microsoft.com to 8.8.8.8
Jun 24 09:58:42 unknown daemon.info dnsmasq[2743]: query[A] storeedgefd.dsx.mp.m                                                            icrosoft.com from 192.168.1.35
Jun 24 09:58:42 unknown daemon.info dnsmasq[2743]: forwarded storeedgefd.dsx.mp.                                                            microsoft.com to 8.8.4.4
Jun 24 09:58:42 unknown daemon.info dnsmasq[2743]: forwarded storeedgefd.dsx.mp.                                                            microsoft.com to 8.8.8.8
Jun 24 09:58:42 unknown daemon.info dnsmasq[2743]: reply storeedgefd.dsx.mp.micr                                                            osoft.com is <CNAME>
Jun 24 09:58:42 unknown daemon.info dnsmasq[2743]: reply storeedgefd.xbetservice                                                            s.akadns.net is <CNAME>
Jun 24 09:58:42 unknown daemon.info dnsmasq[2743]: reply storeedgefd.dsx.mp.micr                                                            osoft.com.edgekey.net is <CNAME>
Jun 24 09:58:42 unknown daemon.info dnsmasq[2743]: reply storeedgefd.dsx.mp.micr                                                            osoft.com.edgekey.net.globalredir.akadns.net is <CNAME>
Jun 24 09:58:42 unknown daemon.info dnsmasq[2743]: reply e16646.dscg.akamaiedge.                                                            net is 23.77.221.224
Jun 24 09:58:45 unknown daemon.info dnsmasq[2743]: query[A] cid-21676d35fb627e59                                                            .users.storage.live.com from 192.168.1.35
Jun 24 09:58:45 unknown daemon.info dnsmasq[2743]: forwarded cid-21676d35fb627e5                                                            9.users.storage.live.com to 8.8.8.8
Jun 24 09:58:45 unknown daemon.info dnsmasq[2743]: query[A] store-images.s-micro                                                            soft.com from 192.168.1.35
Jun 24 09:58:45 unknown daemon.info dnsmasq[2743]: forwarded store-images.s-micr                                                            osoft.com to 8.8.8.8
Jun 24 09:58:45 unknown daemon.info dnsmasq[2743]: reply store-images.s-microsof                                                            t.com is <CNAME>
Jun 24 09:58:45 unknown daemon.info dnsmasq[2743]: reply store-images.s-microsof                                                            t.com-c.edgekey.net is <CNAME>
Jun 24 09:58:45 unknown daemon.info dnsmasq[2743]: reply e12564.dspb.akamaiedge.                                                            net is 23.77.221.160
Jun 24 09:58:45 unknown daemon.info dnsmasq[2743]: query[A] cid-21676d35fb627e59                                                            .users.storage.live.com from 192.168.1.35
Jun 24 09:58:45 unknown daemon.info dnsmasq[2743]: forwarded cid-21676d35fb627e5                                                            9.users.storage.live.com to 8.8.4.4
Jun 24 09:58:45 unknown daemon.info dnsmasq[2743]: forwarded cid-21676d35fb627e5                                                            9.users.storage.live.com to 8.8.8.8
Jun 24 09:58:45 unknown daemon.info dnsmasq[2743]: reply cid-21676d35fb627e59.us                                                            ers.storage.live.com is <CNAME>
Jun 24 09:58:45 unknown daemon.info dnsmasq[2743]: reply odc-routekey-meta-geo.o                                                            nedrive.akadns.net is <CNAME>
Jun 24 09:58:45 unknown daemon.info dnsmasq[2743]: reply odc-routekey-meta-brs.o                                                            nedrive.akadns.net is <CNAME>
Jun 24 09:58:45 unknown daemon.info dnsmasq[2743]: reply odc-common-us-meta.oned                                                            rive.akadns.net.l-0003.dc-msedge.net.l-0003.l-msedge.net is <CNAME>
Jun 24 09:58:45 unknown daemon.info dnsmasq[2743]: reply l-0003.l-msedge.net is                                                             13.107.42.12
Jun 24 09:58:45 unknown daemon.info dnsmasq[2743]: query[A] login.live.com from                                                             192.168.1.35
Jun 24 09:58:45 unknown daemon.info dnsmasq[2743]: forwarded login.live.com to 8                                                            .8.8.8
Jun 24 09:58:45 unknown daemon.info dnsmasq[2743]: forwarded login.live.com to 8                                                            .8.4.4
Jun 24 09:58:46 unknown daemon.info dnsmasq[2743]: query[A] login.live.com from                                                             192.168.1.35
Jun 24 09:58:46 unknown daemon.info dnsmasq[2743]: forwarded login.live.com to 8                                                            .8.8.8
Jun 24 09:58:46 unknown daemon.info dnsmasq[2743]: forwarded login.live.com to 8                                                            .8.4.4
Jun 24 09:58:46 unknown daemon.info dnsmasq[2743]: reply login.live.com is <CNAM                                                            E>
Jun 24 09:58:46 unknown daemon.info dnsmasq[2743]: reply login.msa.msidentity.co                                                            m is <CNAME>
Jun 24 09:58:46 unknown daemon.info dnsmasq[2743]: reply www.tm.lg.prod.aadmsa.a                                                            kadns.net is <CNAME>
Jun 24 09:58:46 unknown daemon.info dnsmasq[2743]: reply prda.aadg.msidentity.co                                                            m is <CNAME>
Jun 24 09:58:46 unknown daemon.info dnsmasq[2743]: reply www.tm.a.prd.aadg.akadn                                                            s.net is 40.126.45.20
Jun 24 09:58:46 unknown daemon.info dnsmasq[2743]: reply www.tm.a.prd.aadg.akadn                                                            s.net is 20.190.173.67
Jun 24 09:58:46 unknown daemon.info dnsmasq[2743]: reply www.tm.a.prd.aadg.akadn                                                            s.net is 40.126.45.18
Jun 24 09:58:46 unknown daemon.info dnsmasq[2743]: reply www.tm.a.prd.aadg.akadn                                                            s.net is 20.190.173.146
Jun 24 09:58:46 unknown daemon.info dnsmasq[2743]: reply www.tm.a.prd.aadg.akadn                                                            s.net is 40.126.45.17
Jun 24 09:58:46 unknown daemon.info dnsmasq[2743]: reply www.tm.a.prd.aadg.akadn                                                            s.net is 20.190.173.144
Jun 24 09:58:46 unknown daemon.info dnsmasq[2743]: reply www.tm.a.prd.aadg.akadn                                                            s.net is 20.190.173.65
Jun 24 09:58:46 unknown daemon.info dnsmasq[2743]: reply www.tm.a.prd.aadg.akadn                                                            s.net is 40.126.45.19
Jun 24 09:58:59 unknown daemon.info dnsmasq[2743]: query[A] lonns3001.accenture.                                                            com from 192.168.1.35
Jun 24 09:58:59 unknown daemon.info dnsmasq[2743]: forwarded lonns3001.accenture                                                            .com to 8.8.4.4
Jun 24 09:58:59 unknown daemon.info dnsmasq[2743]: query[AAAA] lonns3001.accentu                                                            re.com from 192.168.1.35
Jun 24 09:58:59 unknown daemon.info dnsmasq[2743]: forwarded lonns3001.accenture                                                            .com to 8.8.4.4
Jun 24 09:59:03 unknown daemon.info dnsmasq[2743]: query[A] beacons4.gvt2.com fr                                                            om 192.168.1.35
Jun 24 09:59:03 unknown daemon.info dnsmasq[2743]: forwarded beacons4.gvt2.com t                                                            o 8.8.4.4
Jun 24 09:59:03 unknown daemon.info dnsmasq[2743]: reply beacons4.gvt2.com is 21                                                            6.239.32.116
Jun 24 09:59:03 unknown daemon.info dnsmasq[2743]: query[A] beacons.gcp.gvt2.com                                                             from 192.168.1.35
Jun 24 09:59:03 unknown daemon.info dnsmasq[2743]: config beacons.gcp.gvt2.com i                                                            s 0.0.0.0
Jun 24 09:59:03 unknown daemon.info dnsmasq[2743]: query[A] beacons.gvt2.com fro                                                            m 192.168.1.35
Jun 24 09:59:03 unknown daemon.info dnsmasq[2743]: config beacons.gvt2.com is 0.                                                            0.0.0
Jun 24 09:59:03 unknown daemon.info dnsmasq[2743]: query[A] beacons.gvt2.com fro                                                            m 192.168.1.35
Jun 24 09:59:03 unknown daemon.info dnsmasq[2743]: config beacons.gvt2.com is 0.                                                            0.0.0
Jun 24 09:59:15 unknown daemon.info dnsmasq[2743]: query[A] scontent.faep9-2.fna                                                            .fbcdn.net from 192.168.1.35
Jun 24 09:59:15 unknown daemon.info dnsmasq[2743]: forwarded scontent.faep9-2.fn                                                            a.fbcdn.net to 8.8.8.8
Jun 24 09:59:15 unknown daemon.info dnsmasq[2743]: forwarded scontent.faep9-2.fn                                                            a.fbcdn.net to 8.8.4.4
Jun 24 09:59:15 unknown daemon.info dnsmasq[2743]: query[A] scontent.faep9-1.fna                                                            .fbcdn.net from 192.168.1.35
Jun 24 09:59:15 unknown daemon.info dnsmasq[2743]: forwarded scontent.faep9-1.fn                                                            a.fbcdn.net to 8.8.4.4
Jun 24 09:59:15 unknown daemon.info dnsmasq[2743]: reply scontent.faep9-2.fna.fb                                                            cdn.net is 181.30.193.81
Jun 24 09:59:15 unknown daemon.info dnsmasq[2743]: reply scontent.faep9-1.fna.fb                                                            cdn.net is 181.30.193.17
Jun 24 09:59:15 unknown daemon.info dnsmasq[2743]: query[A] www.facebook.com fro                                                            m 192.168.1.35
Jun 24 09:59:15 unknown daemon.info dnsmasq[2743]: cached www.facebook.com is <C                                                            NAME>
Jun 24 09:59:15 unknown daemon.info dnsmasq[2743]: forwarded www.facebook.com to                                                             8.8.4.4
Jun 24 09:59:15 unknown daemon.info dnsmasq[2743]: reply www.facebook.com is <CN                                                            AME>
Jun 24 09:59:15 unknown daemon.info dnsmasq[2743]: reply star-mini.c10r.facebook                                                            .com is 31.13.94.35
Jun 24 09:59:15 unknown daemon.info dnsmasq[2743]: query[A] presence.teams.micro                                                            soft.com from 192.168.1.35
Jun 24 09:59:15 unknown daemon.info dnsmasq[2743]: cached presence.teams.microso                                                            ft.com is <CNAME>
Jun 24 09:59:15 unknown daemon.info dnsmasq[2743]: forwarded presence.teams.micr                                                            osoft.com to 8.8.4.4
Jun 24 09:59:16 unknown daemon.info dnsmasq[2743]: reply presence.teams.microsof                                                            t.com is <CNAME>
Jun 24 09:59:16 unknown daemon.info dnsmasq[2743]: reply presence.services.sfb.t                                                            rafficmanager.net is <CNAME>
Jun 24 09:59:16 unknown daemon.info dnsmasq[2743]: reply a-ups-presence3-prod-az                                                            sc.eastus2.cloudapp.azure.com is 52.114.142.205
Jun 24 09:59:21 unknown daemon.info dnsmasq[2743]: query[A] wpad.accenture.com f                                                            rom 192.168.1.35
Jun 24 09:59:21 unknown daemon.info dnsmasq[2743]: cached wpad.accenture.com is                                                             NXDOMAIN
Jun 24 09:59:25 unknown daemon.info dnsmasq[2743]: query[A] i.instagram.com from                                                             192.168.1.132
Jun 24 09:59:25 unknown daemon.info dnsmasq[2743]: forwarded i.instagram.com to                                                             8.8.4.4
Jun 24 09:59:25 unknown daemon.info dnsmasq[2743]: reply i.instagram.com is <CNA                                                            ME>
Jun 24 09:59:25 unknown daemon.info dnsmasq[2743]: reply instagram.c10r.facebook                                                            .com is 31.13.94.51
Jun 24 09:59:25 unknown daemon.info dnsmasq[2743]: query[A] scontent.cdninstagra                                                            m.com from 192.168.1.132
Jun 24 09:59:25 unknown daemon.info dnsmasq[2743]: forwarded scontent.cdninstagr                                                            am.com to 8.8.4.4
Jun 24 09:59:25 unknown daemon.info dnsmasq[2743]: reply scontent.cdninstagram.c                                                            om is 31.13.94.51
Jun 24 09:59:31 unknown daemon.info dnsmasq[2743]: query[A] ocsp.usertrust.com f                                                            rom 192.168.1.35
Jun 24 09:59:31 unknown daemon.info dnsmasq[2743]: forwarded ocsp.usertrust.com                                                             to 8.8.4.4
Jun 24 09:59:31 unknown daemon.info dnsmasq[2743]: reply ocsp.usertrust.com is 1                                                            51.139.128.14
Jun 24 09:59:32 unknown daemon.info dnsmasq[2743]: query[A] crl.usertrust.com fr                                                            om 192.168.1.35
Jun 24 09:59:32 unknown daemon.info dnsmasq[2743]: forwarded crl.usertrust.com t                                                            o 8.8.4.4
Jun 24 09:59:32 unknown daemon.info dnsmasq[2743]: reply crl.usertrust.com is 15                                                            1.139.128.14
Jun 24 09:59:32 unknown daemon.info dnsmasq[2743]: query[A] ocsp.comodoca.com fr                                                            om 192.168.1.35
Jun 24 09:59:32 unknown daemon.info dnsmasq[2743]: forwarded ocsp.comodoca.com t                                                            o 8.8.4.4
Jun 24 09:59:32 unknown daemon.info dnsmasq[2743]: reply ocsp.comodoca.com is 15                                                            1.139.128.14
Jun 24 09:59:33 unknown daemon.info dnsmasq[2743]: query[A] crl.comodoca.com fro                                                            m 192.168.1.35
Jun 24 09:59:33 unknown daemon.info dnsmasq[2743]: forwarded crl.comodoca.com to                                                             8.8.4.4
Jun 24 09:59:33 unknown daemon.info dnsmasq[2743]: reply crl.comodoca.com is 151                                                            .139.128.14
Jun 24 09:59:33 unknown daemon.info dnsmasq[2743]: query[A] ef710abdc1ea5ec1cc93                                                            74c59652a642.clo.footprintdns.com from 192.168.1.35
Jun 24 09:59:33 unknown daemon.info dnsmasq[2743]: forwarded ef710abdc1ea5ec1cc9                                                            374c59652a642.clo.footprintdns.com to 8.8.4.4
Jun 24 09:59:33 unknown daemon.info dnsmasq[2743]: reply ef710abdc1ea5ec1cc9374c                                                            59652a642.clo.footprintdns.com is <CNAME>
Jun 24 09:59:33 unknown daemon.info dnsmasq[2743]: reply dxb20prdapp02-canary-op                                                            aph.cloudapp.net is 40.123.219.249
Jun 24 09:59:34 unknown daemon.info dnsmasq[2743]: query[A] graph.instagram.com                                                             from 192.168.1.132
Jun 24 09:59:34 unknown daemon.info dnsmasq[2743]: forwarded graph.instagram.com                                                             to 8.8.4.4
Jun 24 09:59:34 unknown daemon.info dnsmasq[2743]: reply graph.instagram.com is                                                             <CNAME>
Jun 24 09:59:34 unknown daemon.info dnsmasq[2743]: reply instagram.c10r.facebook                                                            .com is 31.13.94.51
Jun 24 09:59:35 unknown daemon.info dnsmasq[2743]: query[A] l-ring.msedge.net fr                                                            om 192.168.1.35
Jun 24 09:59:35 unknown daemon.info dnsmasq[2743]: forwarded l-ring.msedge.net t                                                            o 8.8.8.8
Jun 24 09:59:35 unknown daemon.info dnsmasq[2743]: forwarded l-ring.msedge.net t                                                            o 8.8.4.4
Jun 24 09:59:35 unknown daemon.info dnsmasq[2743]: reply l-ring.msedge.net is <C                                                            NAME>
Jun 24 09:59:35 unknown daemon.info dnsmasq[2743]: reply l-ring.l-9999.l-msedge.                                                            net is <CNAME>
Jun 24 09:59:35 unknown daemon.info dnsmasq[2743]: reply l-9999.l-msedge.net is                                                             13.107.42.254
Jun 24 09:59:37 unknown daemon.info dnsmasq[2743]: query[A] outlook.office365.co                                                            m from 192.168.1.35
Jun 24 09:59:37 unknown daemon.info dnsmasq[2743]: forwarded outlook.office365.c                                                            om to 8.8.8.8
Jun 24 09:59:37 unknown daemon.info dnsmasq[2743]: reply outlook.office365.com i                                                            s <CNAME>
Jun 24 09:59:37 unknown daemon.info dnsmasq[2743]: reply outlook.ha.office365.co                                                            m is <CNAME>
Jun 24 09:59:37 unknown daemon.info dnsmasq[2743]: reply outlook.ms-acdc.office.                                                            com is <CNAME>
Jun 24 09:59:37 unknown daemon.info dnsmasq[2743]: reply SCL-efz.ms-acdc.office.                                                            com is 40.102.34.2
Jun 24 09:59:37 unknown daemon.info dnsmasq[2743]: reply SCL-efz.ms-acdc.office.                                                            com is 40.102.33.226
Jun 24 09:59:37 unknown daemon.info dnsmasq[2743]: reply SCL-efz.ms-acdc.office.                                                            com is 52.97.3.130
Jun 24 09:59:37 unknown daemon.info dnsmasq[2743]: reply SCL-efz.ms-acdc.office.                                                            com is 40.102.34.34
Jun 24 09:59:45 unknown daemon.info dnsmasq[2743]: query[A] a03cmg01.accenture.c                                                            om from 192.168.1.35
Jun 24 09:59:45 unknown daemon.info dnsmasq[2743]: cached a03cmg01.accenture.com                                                             is <CNAME>
Jun 24 09:59:45 unknown daemon.info dnsmasq[2743]: forwarded a03cmg01.accenture.                                                            com to 8.8.8.8
Jun 24 09:59:45 unknown daemon.info dnsmasq[2743]: reply a03cmg01.accenture.com                                                             is <CNAME>
Jun 24 09:59:45 unknown daemon.info dnsmasq[2743]: reply a03cmg01.cloudapp.net i                                                            s 23.96.114.53
Jun 24 09:59:46 unknown daemon.info dnsmasq[2743]: query[A] multi-chat.net from                                                             192.168.1.35
Jun 24 09:59:46 unknown daemon.info dnsmasq[2743]: forwarded multi-chat.net to 8                                                            .8.8.8
Jun 24 09:59:46 unknown daemon.info dnsmasq[2743]: reply multi-chat.net is 172.6                                                            7.216.252
Jun 24 09:59:46 unknown daemon.info dnsmasq[2743]: reply multi-chat.net is 104.2                                                            1.61.239
Jun 24 09:59:46 unknown daemon.info dnsmasq[2743]: query[A] multi-chat.net from                                                             192.168.1.35
Jun 24 09:59:46 unknown daemon.info dnsmasq[2743]: cached multi-chat.net is 104.                                                            21.61.239
Jun 24 09:59:46 unknown daemon.info dnsmasq[2743]: cached multi-chat.net is 172.                                                            67.216.252
Jun 24 09:59:46 unknown daemon.info dnsmasq[2743]: query[A] beacons2.gvt2.com fr                                                            om 192.168.1.35
Jun 24 09:59:46 unknown daemon.info dnsmasq[2743]: forwarded beacons2.gvt2.com t                                                            o 8.8.8.8
Jun 24 09:59:46 unknown daemon.info dnsmasq[2743]: reply beacons2.gvt2.com is 17                                                            2.217.24.163
Jun 24 09:59:47 unknown daemon.info dnsmasq[2743]: query[A] vdloader.com from 19                                                            2.168.1.35
Jun 24 09:59:47 unknown daemon.info dnsmasq[2743]: forwarded vdloader.com to 8.8                                                            .8.8
Jun 24 09:59:47 unknown daemon.info dnsmasq[2743]: reply vdloader.com is 172.67.                                                            196.140
Jun 24 09:59:47 unknown daemon.info dnsmasq[2743]: reply vdloader.com is 104.21.                                                            90.73
Jun 24 09:59:52 unknown daemon.info dnsmasq[2743]: query[A] fp-vs-nocache.azuree                                                            dge.net from 192.168.1.35
Jun 24 09:59:52 unknown daemon.info dnsmasq[2743]: forwarded fp-vs-nocache.azure                                                            edge.net to 8.8.8.8
Jun 24 09:59:52 unknown daemon.info dnsmasq[2743]: reply fp-vs-nocache.azureedge                                                            .net is <CNAME>
Jun 24 09:59:52 unknown daemon.info dnsmasq[2743]: reply fp-vs-nocache.ec.azuree                                                            dge.net is <CNAME>
Jun 24 09:59:52 unknown daemon.info dnsmasq[2743]: reply cs9.wpc.v0cdn.net is 15                                                            2.199.55.200
Jun 24 09:59:54 unknown daemon.info dnsmasq[2743]: query[A] settings-win.data.mi                                                            crosoft.com from 192.168.1.35
Jun 24 09:59:54 unknown daemon.info dnsmasq[2743]: forwarded settings-win.data.m                                                            icrosoft.com to 8.8.8.8
Jun 24 09:59:54 unknown daemon.info dnsmasq[2743]: reply settings-win.data.micro                                                            soft.com is <CNAME>
Jun 24 09:59:54 unknown daemon.info dnsmasq[2743]: reply settingsfd-geo.trafficm                                                            anager.net is 52.191.219.104
Jun 24 09:59:54 unknown daemon.info dnsmasq[2743]: query[A] settings-win.data.mi                                                            crosoft.com from 192.168.1.35
Jun 24 09:59:54 unknown daemon.info dnsmasq[2743]: cached settings-win.data.micr                                                            osoft.com is <CNAME>
Jun 24 09:59:54 unknown daemon.info dnsmasq[2743]: cached settingsfd-geo.traffic                                                            manager.net is 52.191.219.104
Jun 24 10:00:02 unknown daemon.info dnsmasq[2743]: query[A] ssl.gstatic.com from                                                             192.168.1.35
Jun 24 10:00:02 unknown daemon.info dnsmasq[2743]: forwarded ssl.gstatic.com to                                                             8.8.8.8
Jun 24 10:00:02 unknown daemon.info dnsmasq[2743]: forwarded ssl.gstatic.com to                                                             8.8.4.4
Jun 24 10:00:02 unknown daemon.info dnsmasq[2743]: reply ssl.gstatic.com is 172.                                                            217.162.3
Jun 24 10:00:05 unknown daemon.info dnsmasq[2743]: query[A] europe.cp.wd.microso                                                            ft.com from 192.168.1.35
Jun 24 10:00:05 unknown daemon.info dnsmasq[2743]: cached europe.cp.wd.microsoft                                                            .com is <CNAME>
Jun 24 10:00:05 unknown daemon.info dnsmasq[2743]: forwarded europe.cp.wd.micros                                                            oft.com to 8.8.8.8
Jun 24 10:00:05 unknown daemon.info dnsmasq[2743]: reply europe.cp.wd.microsoft.                                                            com is <CNAME>
Jun 24 10:00:05 unknown daemon.info dnsmasq[2743]: reply wd-prod-cp-eu.trafficma                                                            nager.net is <CNAME>
Jun 24 10:00:05 unknown daemon.info dnsmasq[2743]: reply wd-prod-cp-eu-north-2-f                                                            e.northeurope.cloudapp.azure.com is 40.113.10.47
Jun 24 10:00:11 unknown daemon.info dnsmasq[2743]: query[A] eu-v20.events.data.m                                                            icrosoft.com from 192.168.1.35
Jun 24 10:00:11 unknown daemon.info dnsmasq[2743]: cached eu-v20.events.data.mic                                                            rosoft.com is <CNAME>
Jun 24 10:00:11 unknown daemon.info dnsmasq[2743]: forwarded eu-v20.events.data.                                                            microsoft.com to 8.8.8.8
Jun 24 10:00:11 unknown daemon.info dnsmasq[2743]: reply eu-v20.events.data.micr                                                            osoft.com is <CNAME>
Jun 24 10:00:11 unknown daemon.info dnsmasq[2743]: reply eu.events.data.trafficm                                                            anager.net is <CNAME>
Jun 24 10:00:11 unknown daemon.info dnsmasq[2743]: reply skypedataprdcolweu01.cl                                                            oudapp.net is 52.114.74.45
"""

#projectlocation= system.os("pwd")
projectlocation= "//opt//python3"


#Definiciiones de servicios a usar
app = Flask(__name__)
#app = Flask(__name__, static_folder='templates\\static\\', static_url_path='/templates/static/')
app.secret_key = 'mysecretkey'

@app.route('/')
def home():
	dhcpd_lease=device_list()
	
	cmd = 'more /var/log/messages | grep "dnsmasq"'
	#proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
	#out, err = proc.communicate()
	
	lines=str(out).count("dnsmasq")
	block=str(out).count("0.0.0.0")
	#output=str(out).replace('b"','').replace("b'",'').split("\\n")
	output=str(out).replace('b"','').replace("b'",'').split("\n")#for testing in Windows
	#print(output)
	first=str(output).split(" unknown")[0].split("'")[1]
	print("first: " + str(first))
	y=datetime.date.today().year
	mon=strptime(first.split(" ")[0],'%b').tm_mon
	d=first.split(" ")[1]
	h=first.split(" ")[2].split(":")[0]
	min=first.split(" ")[2].split(":")[1]
	s=first.split(" ")[2].split(":")[2]
	time0= datetime.datetime(int(y), int(mon), int(d), int(h), int(min), int(s))
	timenow=datetime.datetime.now()
	print("now: " + str(timenow))
	delta=str(timenow-time0).split(":")[0]
	print("Diference is: " + str(delta))
	lines="Logs displayed: " + str(lines)
	block="Queries filtered in last " + str(delta) + " minutes: " + str(block)
	for line in output:
		string=line.strip().replace("unknown daemon.info dnsmasq","")
		try:
			#string=line.split("unknown")[0] + ":" + line
			toprint=string.split(":")
		except:
			flash(string)
		else:
			flash(toprint)
	return render_template("index.html", lines = lines, block = block)

if (__name__ == '__main__'):
    app.run(port=3000, host='0.0.0.0', debug=True)
