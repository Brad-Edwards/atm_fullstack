<!--
  MovieList.vue

    This component acts as the landing page of the application. 
    It lists all movies, provides search functionality and displays 
    a selected movie.
-->
<template>
  <div class="list row">
    <div class="col-md-8">
      <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="Search by title"
          v-model="title" v-on:keyup.enter="searchTitle" v-on:input="searchTitle"/>        
      </div>
    </div>
    <div class="col-md-6">
      <div class="overflow-scroll" style="height: 50rem" >
        <h4>Movies List</h4>
        <ul class="list-group">
          <li class="list-group-item"
            :class="{ active: index == currentIndex }"
            v-for="(movie, index) in movies"
            :key="index"
            @click="setActiveMovie(movie, index)"
          >
            {{ movie.title }} {{ movie.release_year }}
          </li>
        </ul>
      </div>      
    </div>
    <div class="col-md-6">
      <div v-if="currentMovie">
        <h4>Movie</h4>
        <div>
            <img class="img-thumbnail" v-bind:src="currentMovie.poster_uri">
        </div>
        <div>
          <label><strong>Title:</strong></label> {{ currentMovie.title }}
        </div>
        <div>
            <label><strong>Year:</strong></label> {{ currentMovie.release_year }}
        </div>
        <div>
            <label><strong>Duration:</strong></label> {{ currentMovie.duration }} mins.
        </div>
        <div>
          <label><strong>Description:</strong></label> {{ currentMovie.description }}
        </div>               
        <div>
            <router-link :to="'/movies/' + currentMovie.id" class="badge badge-warning" style="color: blue">Edit</router-link>            
        </div>        
        <div>
            <p><input type="radio" name="likeList" value="True" checked="checked"> Like 
            <input type="radio" name="likeList" value="False"> Dislike 
            <button name="rateButton" class="btn btn-success" @click="rateMovie">Rate It!</button></p>
        </div>    
      </div>
      <div v-else>
        <br />
        <p>Please click on a Movie...</p>
      </div>
    </div>
  </div>
</template>

<script>
import MovieDataService from "../services/MovieDataService";
import ReviewDataService from "../services/ReviewDataService.js"

export default {
  name: "movies-list",
  components: {

  },
  data() {
    return {
      movies: [],
      currentMovie: null,
      currentIndex: -1,
      title: "",
      ratings: [],
      likes: 0,
      dislikes: 0,
    };
  },
  methods: {
       rateMovie() {
         // Saves a review to the database.         
        var data = {
            rating: "True",
            movie: this.currentMovie.id,
            date: new Date().toISOString().slice(0, 10),
        };

        ReviewDataService.create(data)
    },
    retrieveMovies() {
      // Gets all movies from the database.
      MovieDataService.getAll()
        .then(response => {
          this.movies = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
    refreshList() {
      // Refreshes the movie list.
      this.retrieveMovies();
      this.currentMovie = null;
      this.currentIndex = -1;
    },
    setActiveMovie(movie, index) {
      // Sets the active movie to display.
      this.currentMovie = movie;
      this.currentIndex = movie ? index : -1;
      this.retrieveRatings();
    },    
    searchTitle() {
      // Searches the database for movies matching 
      // a title
      MovieDataService.findByTitle(this.title)
        .then(response => {
          this.movies = response.data;
          this.setActiveMovie(null);
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    this.retrieveMovies();
  }
};
</script>

<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>