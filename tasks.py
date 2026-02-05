from crewai import Task

class trichytask():
    def holy_place_searcher(self, agent):
        return Task(
            description=(
                "Search for the most famous and popular holy places in {city}. "
                "Include temples, churches, and mosques. "
                "Provide the exact location, address, and any special features of each place."
            ),
            expected_output=(
                "A detailed list of holy places in {city} including:\n"
                "- Name of the place\n"
                "- Type (temple/church/mosque)\n"
                "- Exact address and location\n"
                "- Significance and special features\n"
                "- Visiting hours if available"
            ),
            agent=agent
        )

    def Jewellery_finder(self, agent):
        return Task(
            description=(
                "Find the most famous and reputable jewellery shops in {city}. "
                "Focus on shops with good customer reviews and authentic products."
            ),
            expected_output=(
                "A comprehensive list of jewellery shops including:\n"
                "- Shop name\n"
                "- Exact location and address\n"
                "- Specialties (gold, silver, diamond, etc.)\n"
                "- Customer ratings if available"
            ),
            agent=agent
        )

    def mart_seracher(self, agent):
        return Task(
            description=(
                "Locate popular shopping malls and marts in {city} that are "
                "frequently visited by people. Include both large malls and local markets."
            ),
            expected_output=(
                "A detailed list of shopping marts including:\n"
                "- Name of the mall/mart\n"
                "- Location and landmark\n"
                "- Types of products available\n"
                "- Operating hours\n"
                "- Special features or attractions"
            ),
            agent=agent
        )

    def courier_finder(self, agent):
        return Task(
            description=(
                "Find reliable and secure courier service providers in {city}. "
                "Focus on services that are widely used and have good safety records."
            ),
            expected_output=(
                "A list of courier services with:\n"
                "- Company name\n"
                "- Office locations in {city}\n"
                "- Services offered (domestic/international)\n"
                "- Contact information\n"
                "- Customer ratings for reliability"
            ),
            agent=agent
        )

    def restaurant_suggest(self, agent):
        return Task(
            description=(
                "Identify the best restaurants in {city}. "
                "Include information about their specialties, location, and signature dishes."
            ),
            expected_output=(
                "A curated list of top restaurants featuring:\n"
                "- Restaurant name\n"
                "- Exact location with landmarks\n"
                "- Cuisine type\n"
                "- Best-selling or signature dishes\n"
                "- Price range\n"
                "- Customer ratings"
            ),
            agent=agent
        )

    def suggest_auto(self, agent):
        return Task(
            description=(
                "Locate the best automobile service centers in {city}. "
                "Include authorized service centers for major brands."
            ),
            expected_output=(
                "A comprehensive list of service centers with:\n"
                "- Service center name\n"
                "- Exact address\n"
                "- Brands serviced\n"
                "- Opening and closing times\n"
                "- Contact information\n"
                "- Services offered (maintenance, repairs, etc.)"
            ),
            agent=agent
        )

    def suggest_homeappl(self, agent):
        return Task(
            description=(
                "Find the best home appliances stores in {city}. "
                "Include both authorized dealers and multi-brand outlets."
            ),
            expected_output=(
                "A detailed list of home appliance stores including:\n"
                "- Store name\n"
                "- Exact address and location\n"
                "- Brands available\n"
                "- Opening and closing times\n"
                "- Special offers or services (warranty, installation, etc.)"
            ),
            agent=agent
        )

    def entertainment_task(self, agent):
        return Task(
            description=(
                "Locate the most popular and highly-rated parks and theaters in {city}. "
                "Focus on places with positive reviews and good facilities."
            ),
            expected_output=(
                "A list of entertainment venues with:\n"
                "- Name of park/theater\n"
                "- Exact location\n"
                "- Facilities available\n"
                "- Ratings and reviews\n"
                "- Entry fees if applicable\n"
                "- Show timings for theaters"
            ),
            agent=agent
        )

    def vessel_shop_task(self, agent):
        return Task(
            description=(
                "Find shops specializing in kitchenware and vessels in {city}. "
                "Include shops with wide variety and good quality products."
            ),
            expected_output=(
                "A list of kitchenware shops including:\n"
                "- Shop name\n"
                "- Exact location with landmarks\n"
                "- Types of products available\n"
                "- Price range\n"
                "- Customer reviews"
            ),
            agent=agent
        )

    def stationary_shop_task(self, agent):
        return Task(
            description=(
                "Locate reputable stationary shops in {city} known for "
                "quality products and good variety."
            ),
            expected_output=(
                "A detailed list of stationary shops with:\n"
                "- Shop name\n"
                "- Location with landmarks\n"
                "- Product range (office supplies, school supplies, etc.)\n"
                "- Special features (printing services, binding, etc.)"
            ),
            agent=agent
        )

    def photoshop_task(self, agent):
        return Task(
            description=(
                "Find reliable photo studios in {city} with good "
                "customer reviews and quality services."
            ),
            expected_output=(
                "A list of photo studios featuring:\n"
                "- Studio name\n"
                "- Exact location\n"
                "- Services offered (portraits, events, commercial, etc.)\n"
                "- Customer reviews\n"
                "- Contact information\n"
                "- Price range"
            ),
            agent=agent
        )

    def hospital_suggester(self, agent):
        return Task(
            description=(
                "Identify the best hospitals in {city} with information "
                "about their specializations and facilities."
            ),
            expected_output=(
                "A comprehensive list of hospitals including:\n"
                "- Hospital name\n"
                "- Exact location and address\n"
                "- Specialized treatments and departments\n"
                "- Emergency services availability\n"
                "- Contact information\n"
                "- Facilities available"
            ),
            agent=agent
        )

    def finding_IT_companies(self, agent):
        return Task(
            description=(
                "Search for top IT companies located in {city}. "
                "Include both product and service-based companies."
            ),
            expected_output=(
                "A list of IT companies with:\n"
                "- Company name\n"
                "- Location in {city}\n"
                "- Company size and type\n"
                "- Services/products offered\n"
                "- Career opportunities if available"
            ),
            agent=agent
        )

    def finding_Automobiles_companies(self, agent):
        return Task(
            description=(
                "Search for top automobile companies and dealerships in {city}. "
                "Include manufacturers, dealers, and related businesses."
            ),
            expected_output=(
                "A list of automobile companies featuring:\n"
                "- Company name\n"
                "- Location and address\n"
                "- Brands represented\n"
                "- Services offered (sales, service, parts)\n"
                "- Contact information"
            ),
            agent=agent
        )

    def locating_display_furniture(self, agent):
        return Task(
            description=(
                "Find the top furniture shops in {city} with good "
                "variety and quality products."
            ),
            expected_output=(
                "A detailed list of furniture shops including:\n"
                "- Shop name\n"
                "- Exact location\n"
                "- Types of furniture available\n"
                "- Price range\n"
                "- Custom furniture options\n"
                "- Delivery services"
            ),
            agent=agent
        )

    def discovering_gift_shops(self, agent):
        return Task(
            description=(
                "Locate the best gift shops in {city} offering unique "
                "and diverse gift options."
            ),
            expected_output=(
                "A list of gift shops with:\n"
                "- Shop name\n"
                "- Location with landmarks\n"
                "- Types of gifts available\n"
                "- Price range\n"
                "- Special services (gift wrapping, customization, etc.)"
            ),
            agent=agent
        )

    def text_task(self, agent):
        return Task(
            description=(
                "Find famous textile shops in {city} offering quality "
                "fabrics for both men and women."
            ),
            expected_output=(
                "A comprehensive list of textile shops including:\n"
                "- Shop name\n"
                "- Exact location\n"
                "- Types of fabrics available\n"
                "- Quality indicators\n"
                "- Price range\n"
                "- Special collections"
            ),
            agent=agent
        )

    def par_task(self, agent):
        return Task(
            description=(
                "Locate famous beauty parlours in {city} offering grooming "
                "and bridal makeup services for both men and women."
            ),
            expected_output=(
                "A detailed list of beauty parlours with:\n"
                "- Parlour name\n"
                "- Location and address\n"
                "- Services offered\n"
                "- Specialties (bridal makeup, grooming, etc.)\n"
                "- Price range\n"
                "- Customer reviews"
            ),
            agent=agent
        )

    def skl_task(self, agent):
        return Task(
            description=(
                "Find the best schools in {city} with information about "
                "their facilities and academic performance."
            ),
            expected_output=(
                "A list of top schools including:\n"
                "- School name\n"
                "- Location and address\n"
                "- Board affiliation (CBSE, ICSE, State, etc.)\n"
                "- Facilities available\n"
                "- Academic reputation\n"
                "- Contact information"
            ),
            agent=agent
        )

    def clg_task(self, agent):
        return Task(
            description=(
                "Find the best colleges in {city} including engineering, "
                "arts, science, and professional colleges."
            ),
            expected_output=(
                "A comprehensive list of colleges with:\n"
                "- College name\n"
                "- Location and address\n"
                "- Courses offered\n"
                "- Accreditation and affiliations\n"
                "- Facilities and infrastructure\n"
                "- Admission information"
            ),
            agent=agent
        )

    def tour_task(self, agent):
        return Task(
            description=(
                "Identify famous tourist places in {city} with exact "
                "locations and visitor information."
            ),
            expected_output=(
                "A detailed list of tourist attractions including:\n"
                "- Place name\n"
                "- Exact location and how to reach\n"
                "- Historical or cultural significance\n"
                "- Entry fees and timings\n"
                "- Best time to visit\n"
                "- Nearby attractions"
            ),
            agent=agent
        )

    def stay_suggest(self, agent):
        return Task(
            description=(
                "Find the best accommodation options in {city} including "
                "hotels, lodges, and guest houses."
            ),
            expected_output=(
                "A curated list of staying options with:\n"
                "- Accommodation name\n"
                "- Exact location\n"
                "- Room types available\n"
                "- Price range\n"
                "- Facilities and amenities\n"
                "- Customer ratings\n"
                "- Contact information"
            ),
            agent=agent
        )