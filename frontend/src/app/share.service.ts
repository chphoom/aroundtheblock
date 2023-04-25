import { Injectable } from '@angular/core';
import { Observable, BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ShareService {

  constructor() { }

  private currentValueSubject = new BehaviorSubject<any>(null);

  setCurrentValue(value: any) {
    this.currentValueSubject.next(value);
  }

  getCurrentValue(): Observable<any> {
    return this.currentValueSubject.asObservable();
  }
}