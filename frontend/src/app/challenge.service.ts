import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, map, filter, from, last, throwError } from 'rxjs';
import { Challenge } from './models';
export { Challenge } from './models';

@Injectable({
  providedIn: 'root'
})
export class ChallengeService {

  constructor(private http: HttpClient) {}

  /**
   * Retrieve all Challenges in the system.
   * 
   * @returns an observable array of Challenge objects.
   */
  getAllChallenges(): Observable<Challenge[]> {
    return this.http.get<Challenge[]>("/api/challenges");
  }

  /**
   * Retrieve current weChallenge.
   * 
   * @returns a the most recent weChallenge.
   */
  getCurrentChallenge(): Observable<Challenge> {
    return this.http.get<Challenge>("api/current")
  }

  /**
   * Retrieve all weChallenges.
   * 
   * @returns an observable array of Challenge objects.
   */
  getWeChallenges(): Observable<Challenge[]> {
    return this.http.get<Challenge[]>("/api/wechallenges");
  }

  /**
   * Retrieve all meChallenges.
   * 
   * @returns an observable array of Challenge objects.
   */
  getMeChallenges(): Observable<Challenge[]> {
    return this.http.get<Challenge[]>("/api/mechallenges");
  }

  /**
   * Retrieve all meChallenges.
   * 
   * @returns an observable array of Challenge objects.
   */
  createChallenge(options: Array<String>): Observable<Challenge> {
    return this.http.post<Challenge>("/api/challenges", 
      {
        "noun": options[0],
        "verb": options[1],
        "adj": options[2],
        "last_name": options[3],
        "emotion": options[4],
        "style": options[5],
        "colors": options[6],
      }
    );
  }

}
