//
//  IMGViewController.m
//  Birdazam
//
//  Created by Talha Ansari on 4/3/14.
//  Copyright (c) 2014 com.tja2117. All rights reserved.
//

#import "IMGViewController.h"

@interface IMGViewController ()

@end

@implementation IMGViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    self.view.backgroundColor = [UIColor yellowColor];
    
    UIButton *recordButton = [UIButton buttonWithType:UIButtonTypeRoundedRect];
    recordButton.frame = CGRectMake(100, 200, 100, 50);
    [recordButton setTitle:@"Record" forState:UIControlStateNormal];
    [self.view addSubview:recordButton];
}

- (void) loadView
{
    UIScreen *screen = [UIScreen mainScreen];
    CGRect viewRect = [screen bounds];
    UIView *colorView = [[UIView alloc] initWithFrame:viewRect];
    self.view = colorView;
    
}

- (void) touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event
{
    NSLog(@"Touching began!");
}

- (void) touchesMoved:(NSSet *)touches withEvent:(UIEvent *)event
{
    NSLog(@"Touching moved!");
}

- (void) touchesEnded:(NSSet *)touches withEvent:(UIEvent *)event
{
    NSLog(@"Touches ended!");
}

- (void) touchesCancelled:(NSSet *)touches withEvent:(UIEvent *)event
{
    NSLog(@"Touches cancelled!");
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
