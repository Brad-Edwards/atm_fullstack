import http from "../../http-common";

class ReviewDataService {
  /*
    Handles the exchange of review data with 
    the database.
  */
  create(data) {
    http.post("/reviews", data);
  }
}

export default new ReviewDataService();