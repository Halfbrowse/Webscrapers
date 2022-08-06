import scrapy


class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["be.indeed.com"]
    start_urls = ["https://be.indeed.com/jobs-in-belgium"]

    def parse(self, response):

        for jobs in response.xpath("//ul[@class='jobsearch-ResultsList css-0']/li"):

            Job_Title = jobs.xpath(
                "normalize-space(.//td[@class='resultContent']/div/h2/a/span/text())"
            ).get()
            if Job_Title is None:
                Job_Title = "No Title available"
            Company_Name = jobs.xpath(
                "normalize-space(.//div[@class='heading6 company_location tapItem-gutter companyInfo']/span/a/text())"
            ).get()
            if Company_Name is None:
                Company_Name = "No Company Name available"
            Company_Rating = jobs.xpath(
                "normalize-space(.//span[@class='ratingsDisplay withRatingLink']/text())"
            ).get()
            if Company_Rating is None:
                Company_Rating = "No Company Rating available"
            Company_Location = jobs.xpath(
                "normalize-space(.//div[@class='companyLocation']/text())"
            ).get()
            if Company_Location is None:
                Company_Location = "No Company Location available"
            Meta_data = jobs.xpath(
                "normalize-space(.//div[@class='metadata']/div/text())"
            ).get()
            if Meta_data is None:
                Meta_data = "No Job Type available"
            Job_desc = jobs.xpath(
                "normalize-space(.//div[@class='job-snippet']/ul/li/text())"
            ).get()
            if Job_desc is None:
                Job_desc = "No Job Description available"
            Date_Posted = jobs.xpath(
                "normalize-space(.//span[@class='date']/text())"
            ).get()
            if Date_Posted is None:
                Date_Posted = jobs.xpath(
                    "normalize-space(.//span[@class='myJobsState']/text())"
                ).get()
                if Date_Posted is None:
                    Date_Posted = "Date Posted not available"

            yield {
                "Job Title": Job_Title,
                "Company Name": Company_Name,
                "Company Rating": Company_Rating,
                "Company Location": Company_Location,
                "Job Type": Meta_data,
                "Job Description": Job_desc,
                "Date Posted": Date_Posted,
            }

        next_page = response.xpath(".//a[@aria-label='Next']/@href").get()

        if next_page:
            absolute_url = f"https://be.indeed.com{next_page}"
            yield scrapy.Request(url=absolute_url, callback=self.parse)


# TO DO GO TO https://www.indeed.com/worldwide GET ALL LINKS, WHEN NEXT PAGE IS NONE FOLLOW NEXT LINK.
