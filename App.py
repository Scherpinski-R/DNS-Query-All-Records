import httpx

import dns.query
import dns.message
import dns.rdatatype

class App:
    def __init__(self, url:str, server:str) -> None:
        self.url = self.set_url(url)
        self.server = self.set_server(server)

        # TODO: Get config from file, which queries user wants?
        self.query_types = [
                                dns.rdatatype.TYPE0,
                                dns.rdatatype.NONE,
                                dns.rdatatype.A,
                                dns.rdatatype.NS,
                                dns.rdatatype.MD,
                                dns.rdatatype.MF,
                                dns.rdatatype.CNAME,
                                dns.rdatatype.SOA,
                                dns.rdatatype.MB,
                                dns.rdatatype.MG,
                                dns.rdatatype.MR,
                                dns.rdatatype.NULL,
                                dns.rdatatype.WKS,
                                dns.rdatatype.PTR,
                                dns.rdatatype.HINFO,
                                dns.rdatatype.MINFO,
                                dns.rdatatype.MX,
                                dns.rdatatype.TXT,
                                dns.rdatatype.RP,
                                dns.rdatatype.AFSDB,
                                dns.rdatatype.X25,
                                dns.rdatatype.ISDN,
                                dns.rdatatype.RT,
                                dns.rdatatype.NSAP,
                                dns.rdatatype.NSAP_PTR,
                                dns.rdatatype.SIG,
                                dns.rdatatype.KEY,
                                dns.rdatatype.PX,
                                dns.rdatatype.GPOS,
                                dns.rdatatype.AAAA,
                                dns.rdatatype.LOC,
                                dns.rdatatype.NXT,
                                dns.rdatatype.SRV,
                                dns.rdatatype.NAPTR,
                                dns.rdatatype.KX,
                                dns.rdatatype.CERT,
                                dns.rdatatype.A6,
                                dns.rdatatype.DNAME,
                                dns.rdatatype.OPT,
                                dns.rdatatype.APL,
                                dns.rdatatype.DS,
                                dns.rdatatype.SSHFP,
                                dns.rdatatype.IPSECKEY,
                                dns.rdatatype.RRSIG,
                                dns.rdatatype.NSEC,
                                dns.rdatatype.DNSKEY,
                                dns.rdatatype.DHCID,
                                dns.rdatatype.NSEC3,
                                dns.rdatatype.NSEC3PARAM,
                                dns.rdatatype.TLSA,
                                dns.rdatatype.SMIMEA,
                                dns.rdatatype.HIP,
                                dns.rdatatype.NINFO,
                                dns.rdatatype.CDS,
                                dns.rdatatype.CDNSKEY,
                                dns.rdatatype.OPENPGPKEY,
                                dns.rdatatype.CSYNC,
                                dns.rdatatype.ZONEMD,
                                dns.rdatatype.SVCB,
                                dns.rdatatype.HTTPS,
                                dns.rdatatype.SPF,
                                dns.rdatatype.UNSPEC,
                                dns.rdatatype.NID,
                                dns.rdatatype.L32,
                                dns.rdatatype.L64,
                                dns.rdatatype.LP,
                                dns.rdatatype.EUI48,
                                dns.rdatatype.EUI64,
                                dns.rdatatype.TKEY,
                                dns.rdatatype.TSIG,
                                dns.rdatatype.IXFR,
                                dns.rdatatype.AXFR,
                                dns.rdatatype.MAILB,
                                dns.rdatatype.MAILA,
                                dns.rdatatype.ANY,
                                dns.rdatatype.URI,
                                dns.rdatatype.CAA,
                                dns.rdatatype.AVC,
                                dns.rdatatype.AMTRELAY,
                                dns.rdatatype.TA,
                                dns.rdatatype.DLV,
                        ]
    
    # TODO: Validation
    def set_url(self, url):
        return url

    # TODO: Validation
    def set_server(self, server):
        return server

    def run(self):

        with httpx.Client() as client:
            queries = [ dns.message.make_query(self.url, q) for q in self.query_types ]
            # TODO: Run Threads if slow
            responses = [ dns.query.https(q, self.server, session=client) for q in queries ] 

        list_answers = []
        for r in responses:
            for answer in r.answer:
                list_answers.append(answer)

        print("Showing Responses: \n")
        for answer in list_answers:
            if answer != "":
                print(answer)
