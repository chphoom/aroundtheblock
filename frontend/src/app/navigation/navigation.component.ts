import { Component, ElementRef, ViewChild } from '@angular/core';
import { RegistrationService } from '../registration.service';
import { User } from '../registration.service';
import { Router } from '@angular/router';
import { NotificationService, Notification } from '../notification.service';
import { PostsService } from '../posts.service';
import { CommentService, Comment } from '../comment.service';
import { Observable, map, of, shareReplay } from 'rxjs';
import { ChallengeService, Challenge } from '../challenge.service';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css']
})
export class NavigationComponent {
  public notifs!: Notification[]
  numUnread!: number;
  public user: User | undefined;
  // public countdownMap: Map<number, string> = new Map<number, string>();
  @ViewChild('search', { static: true }) search!: ElementRef;

  constructor(private router: Router,
     public registration_service: RegistrationService,
     public notificationService: NotificationService,
     private commentService: CommentService,
     private challengeService: ChallengeService) {
    this.registration_service.getUserInfo().subscribe((user: User) => {
      this.user = user;
      this.notificationService.getToUser(user.email).subscribe(
        (_Ns: Notification[]) => {
          this.notifs = _Ns;
          of(this.notifs.filter(n => !n.read).length).subscribe(
            (num: number) => {
              this.numUnread = num;
            }
          )
        }
      )
    });
  }

  onSearch() {
    const query = this.search.nativeElement.value;
    // For example, you could navigate to the search page and pass the search term as a query parameter
    this.router.navigate(['/search', query]);  }

    onClickN(notif: Notification) {
      if (notif.comment_id) {
        this.notificationService.read(notif.id!).subscribe(
          (update: Notification) => {
            this.commentService.get(update.comment_id!).subscribe(
              (comment: Comment) => {
                this.router.navigate(['/post', comment.post]).then(() => {
                  // The navigation has completed, so you can safely perform any post-navigation actions here
                });
              }
            )
          }
        )
      } else if (notif.challenge_id) {
        this.router.navigate(['/we-challenge']);
      } else {
        // handle some error idk
      }
    }
    
  private userCache: { [key: string]: Observable<string> } = {};

  getUsername(notif: Notification): Observable<string> {
    const cachedValue = this.userCache[notif.fromUser_id!];
    if (cachedValue) {
      return cachedValue;
    }
    const newValue = this.registration_service.getUser(notif.fromUser_id!).pipe(
      map(user => user ? `${user.displayName}` : ''),
      shareReplay(1) // cache the result
    );
    this.userCache[notif.fromUser_id!] = newValue;
    return newValue;
  }

  logOut() {
    this.registration_service.logout();
    this.router.navigate(['/']);
  }

  // public getCountdown(challengeId: number): string {
  //   // Check if countdown value is already stored in the map
  //   if (this.countdownMap.has(challengeId)) {
  //     return this.countdownMap.get(challengeId)!;
  //   }

  //   // Fetch the saved challenge data based on the challengeId
  //   let savedChallenge: Challenge;
  //   this.challengeService.getChallenge(challengeId).subscribe(
  //     (res:Challenge) => {
  //       savedChallenge = res;
  //     }
  //   );

  //   if (savedChallenge!) {
  //     const end = new Date(savedChallenge.end!).getTime(); // Access the 'end' property from 'current'
  //     setInterval(() => {
  //       const now = new Date().getTime();
  //       const distance = end - now;
  //       const days = Math.floor(distance / (1000 * 60 * 60 * 24)).toString().padStart(2, '0');
  //       const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)).toString().padStart(2, '0');
  //       const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60)).toString().padStart(2, '0');
  //       const seconds = Math.floor((distance % (1000 * 60)) / 1000).toString().padStart(2, '0');
  //       const countdown = days + ':' + hours + ':' + minutes + ':' + seconds;

  //       // Store the countdown value in the map
  //       this.countdownMap.set(challengeId, countdown);
  //     }, 1000);

  //     return ''; // Initially return empty string until the countdown value is calculated
  //   }

  //   return ''; // Handle the case when savedChallenge is not found or null
  // }
}
