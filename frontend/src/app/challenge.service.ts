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
    return this.http.get<Challenge>("api/challenges/current")
  }

  /**
   * Retrieve all weChallenges.
   * 
   * @returns an observable array of Challenge objects.
   */
  getWeChallenges(): Observable<Challenge[]> | null {
    let challenges = this.http.get<Challenge[]>("/api/challenges");
    return challenges.pipe(map(challenges => challenges.filter(challenges => challenges.type = "we")));
  }

  /**
   * Retrieve all meChallenges.
   * 
   * @returns an observable array of Challenge objects.
   */
  getMeChallenges(): Observable<Challenge[]> | null {
    let challenges = this.http.get<Challenge[]>("/api/challenges");
    return challenges.pipe(map(challenges => challenges.filter(challenges => challenges.type = "me")));
  }

}
