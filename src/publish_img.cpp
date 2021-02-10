#include <ros/ros.h>
#include <sensor_msgs/Image.h>
#include <std_srvs/SetBool.h>


class ImgPublisher {

    private:
    int counter;
    ros::Publisher pub;
    ros::Subscriber sub;
    ros::ServiceServer reset_service;

    public:
    ImgPublisher(ros::NodeHandle *nh){
        counter = 0;
        // image = 0;
        sub = nh-> subscribe("/camera/rgb/image_rect_color",1, 
            &ImgPublisher::call_receive_rgb_img, this);

        pub = nh-> advertise<sensor_msgs::Image>("/custom_img",1);

        reset_service = nh->advertiseService("/reset_counter",
            &ImgPublisher::call_reset_counter, this);

    }

    void call_receive_rgb_img(const sensor_msgs::Image img){
        counter += 1;
        // cout << counter;
        ROS_INFO("Message received:");
        pub.publish(img);
    }

    bool call_reset_counter(std_srvs::SetBool::Request &req,
                            std_srvs::SetBool::Response &res)
    {
        if(req.data){
            counter = 0;
            res.success = true;
            res.message = "Counter reset";
        }else{
            res.success = false;
            res.message = "Counter NOT reset";
        }
        return true;
    }

};

int main (int argc, char **argv){
    ros::init(argc, argv, "publish_img");
    // ros::NodeHandle nh;
    ROS_INFO(" test:");
    // ImgPublisher ip = ImgPublisher(&nh);
    // ros::spin();
}